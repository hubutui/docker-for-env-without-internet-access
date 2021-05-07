#
# see also https://github.com/oracle/docker-images/blob/master/OracleLinuxDevelopers/oraclelinux8/python/3.8/Dockerfile
# and https://github.com/oracle/docker-images/blob/master/OracleInstantClient/oraclelinux8/21/Dockerfile
# and https://yum.oracle.com/getting-started.html#installing-software-from-oracle-linux-yum-server
#
FROM oraclelinux:8-slim
ARG PYPI_URL=https://mirrors.aliyun.com/pypi/simple/
RUN microdnf install \
    oracle-epel-release-el8 \
    oracle-instantclient-release-el8 \
    && microdnf install \
    iputils \
    oracle-instantclient-basic \
    oracle-instantclient-sqlplus \
    parallel \
    python38-pip \
    telnet \
    && microdnf clean all
RUN pip3 install --no-cache-dir -i ${PYPI_URL} \
    cx_oracle \
    modin[ray] \
    pymysql \
    sqlalchemy
