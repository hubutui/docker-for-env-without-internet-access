#
# see also https://github.com/oracle/docker-images/blob/master/OracleLinuxDevelopers/oraclelinux8/python/3.8/Dockerfile
# and https://github.com/oracle/docker-images/blob/master/OracleInstantClient/oraclelinux8/21/Dockerfile
#
FROM oraclelinux:8-slim
RUN microdnf install \
    oracle-instantclient-release-el8 \
    && microdnf install \
    iputils \
    oracle-instantclient-basic \
    oracle-instantclient-sqlplus \
    python38-pip \
    telnet \
    && pip3 install --no-cache-dir \
    cx_oracle \
    modin \
    ray \
    sqlalchemy \
    && microdnf clean all
