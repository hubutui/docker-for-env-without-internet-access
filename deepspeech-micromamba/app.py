#!/usr/bin/env python3
#
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import deepspeech
import wave
import subprocess
import numpy as np
import shlex
import uvicorn
import os
from pathlib import Path
import tempfile
import aiohttp
from aiohttp.client_exceptions import ClientError
import logging
from numpy.typing import NDArray

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def convert_samplerate(
    audio_path: os.PathLike, desired_sample_rate: int = 16000
) -> NDArray[np.int16]:
    """调用 sox 命令转换采样频率

    :param audio_path: 输入音频文件路径
    :type audio_path: os.PathLike
    :param desired_sample_rate: 期望的采样频率，默认为16000
    :type desired_sample_rate: int
    :return: 转换好采样频率的音频
    :rtype: NDArray[np.int16]
    """
    sox_cmd = f"sox {audio_path} --type raw --bits 16 --channels 1 --rate {desired_sample_rate} --encoding signed-integer --endian little --compression 0.0 --no-dither - "

    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"SoX returned non-zero status: {e.stderr}")
    except OSError as e:
        raise OSError(
            e.errno,
            f"SoX not found, use {desired_sample_rate}hz files or install it: {e.strerror}",
        )

    return np.frombuffer(output, np.int16)


app = FastAPI()
model_file = "models/deepspeech-0.9.3-models.pbmm"
scorer_file = "models/deepspeech-0.9.3-models.scorer"
ds = deepspeech.Model(model_file)
ds.enableExternalScorer(scorer_file)


async def speech_to_text(file: UploadFile) -> dict:
    """语音转文本

    :param file: 输入音频文件
    :type file: UploadFile
    :return: 输出文本字典，形如：{"text": "hello world"}
    :rtype: dict
    """
    with wave.open(file.file, "rb") as fin:
        # 检查采样频率是否匹配
        fs_orig = fin.getframerate()
        desired_sample_rate = ds.sampleRate()
        if fs_orig != desired_sample_rate:
            # 不匹配的时候调用 sox 来转换
            logger.warning(
                f"Warning: original sample rate ({fs_orig}) is different than {desired_sample_rate}hz. Resampling might produce erratic speech recognition."
            )
            # 创建临时文件目录来保存文件到磁盘，sox 命令需要输入文件
            tempdir = tempfile.TemporaryDirectory()
            temp_file = Path(f"{tempdir.name}/{file.filename}")
            # 特别注意这里要把文件指针移动到文件开头，否则读取的不对．
            # 因为前面有了对 file 的读取操作，文件指针不在文件起始位置了
            await file.seek(0)
            content = await file.read()
            with open(temp_file, "wb") as f:
                f.write(content)
            audio = convert_samplerate(temp_file, desired_sample_rate)
            # 最后清理掉临时目录
            tempdir.cleanup()
        else:
            audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    text = ds.stt(audio)

    return {"text": text}


@app.post("/stt")
async def convert_speech_to_text(file: UploadFile = File(...)):
    try:
        # 创建异步客户端会话
        async with aiohttp.ClientSession() as session:
            # 调用异步函数进行转换
            result = await speech_to_text(file)
            return result
    except ClientError as e:
        return JSONResponse(
            status_code=400, content={"error": f"ClientError: {str(e)}"}
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
