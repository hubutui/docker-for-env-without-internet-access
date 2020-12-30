ARG PYTORCH_VERSION=1.6.0
ARG CUDA_VERSION=10.1
ARG CUDNN_VERSION=7
FROM pytorch/pytorch:${PYTORCH_VERSION}-cuda${CUDA_VERSION}-cudnn${CUDNN_VERSION}-devel as build
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    git \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
ARG PYPI_URL=https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --disable-pip-version-check --no-cache-dir \
    -i ${PYPI_URL} \
    -r /tmp/requirements.txt
ENV FORCE_CUDA=1
ENV TORCH_CUDA_ARCH_LIST="6.1;7.0;7.5"
RUN git clone https://github.com/NVIDIA/apex.git /apex
WORKDIR /apex
RUN MAX_JOBS=4 pip install -v --disable-pip-version-check --no-cache-dir \
    -i ${PYPI_URL} \
    --global-option="--cpp_ext" --global-option="--cuda_ext" .

FROM pytorch/pytorch:${PYTORCH_VERSION}-cuda${CUDA_VERSION}-cudnn${CUDNN_VERSION}-runtime
COPY --from=build /opt/conda /opt/conda
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*