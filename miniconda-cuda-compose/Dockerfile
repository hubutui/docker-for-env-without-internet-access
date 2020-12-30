ARG CUDA_TAG=10.2-runtime-ubuntu18.04
ARG MINICONDA_VERSION=4.8.3
FROM continuumio/miniconda3:${MINICONDA_VERSION} as miniconda3
FROM nvidia/cuda:${CUDA_TAG}
COPY --from=miniconda3 /opt/conda /opt/conda
ENV PATH /opt/conda/bin:$PATH
