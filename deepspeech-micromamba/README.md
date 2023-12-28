# DeepSpeech Dockerfile

## 简介

这个例子创建了一个基于 fastapi 的语音识别服务．其中，语音识别由 [DeepSpeech](https://github.com/mozilla/DeepSpeech)．

DeepSpeech 只支持 CUDA 10.1 和 Python 3.9，为了避免从源码开始编译．我们选择使用 NVIDIA NGC 的 cuda 镜像作为基础镜像．同时还使用 micromamba 替代 conda，作为演示例子．

## 使用

从 Dockerfile 构建镜像：

```bash
docker build -t deepspeech:gpu .
```

从 [Github](https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3) 上下载 DeepSpeech 所需的 model 和 scorer 文件，并相应地修改 `app.py` 中的路径，然后使用创建好的镜像来启动一个容器：

```bash
docker run -d --rm -p 8080:8080 --gpus all -v ${PWD}:/app deepspeech:gpu
```

这个时候访问 `http://localhost:8080/docs` 即可看到对应的文档并进行测试了．或者自己按照文档，发送请求即可．
