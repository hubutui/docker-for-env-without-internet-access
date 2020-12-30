ARG CUDA_TAG=10.2-runtime-ubuntu18.04
FROM nvidia/cuda:${CUDA_TAG}
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates
ARG URL=https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN curl -o ~/miniconda.sh ${URL} \
    && bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh
ENV PATH /opt/conda/bin:$PATH
