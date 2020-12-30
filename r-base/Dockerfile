ARG R_VERSION=3.6.1

FROM r-base:${R_VERSION}
COPY requirements.R /tmp/requirements.R
RUN Rscript /tmp/requirements.R