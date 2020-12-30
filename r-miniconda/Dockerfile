ARG MINICONDA_VERSION=4.8.3

FROM continuumio/miniconda3:${MINICONDA_VERSION}

ARG R_VERSION=3.6.1
RUN conda install -c r -y \
    r-base=${R_VERSION} \
    r-ggplot2 \
    r-openxlsx \
    && conda clean -afy