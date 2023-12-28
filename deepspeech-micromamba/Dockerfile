FROM mambaorg/micromamba:1.5-alpine as micromamba
FROM nvcr.io/nvidia/cuda:10.1-cudnn7-runtime-rockylinux8
ENV MAMBA_ROOT_PREFIX="/opt/conda"
ENV MAMBA_EXE="/bin/micromamba"
COPY --from=micromamba "$MAMBA_EXE" "$MAMBA_EXE"

ARG PYPI_MIRROR=https://mirrors.sustech.edu.cn/pypi/simple
RUN micromamba install -n base -c conda-forge -y \
    aiohttp \
    fastapi \
    python-multipart \
    python=3.9 \
    sox \
    uvicorn \
    && micromamba clean -afy \
    && micromamba run -n base pip install --no-cache-dir \
    --index-url ${PYPI_MIRROR} \
    deepspeech-gpu
EXPOSE 8080
WORKDIR /app
ENTRYPOINT [ "micromamba", "run", "-n", "base", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "app:app" ]