以 [Oracle Linux](https://hub.docker.com/_/oraclelinux/) 为基础镜像，提供了 Oracle 数据库开发的基础工具，包括：

1. 访问 Oracle 数据库所需的客户端：
   - Oracle Instant Client
   - SQLPlUS
2. 访问 Oracle 数据库所需 Python 接口：cx_Oracle
3. 测试网络的 `ping` 和 `telnet`
4. pandas, modin, ray 和 SQLAlchemy

要构建此镜像，请运行：

```bash
docker build -t oracle-database .
```

Oracle 提供的 Dockerfile 见 https://github.com/oracle/docker-images．