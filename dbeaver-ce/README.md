这个镜像提供了 DBeaver，并预装了数据库驱动文件．此镜像要求宿主机安装 [x11docker](https://github.com/mviereck/x11docker) 及其依赖．要构建此镜像，请运行：

```bash
docker build -t sribd-dbeaver-ce .
```

要从构建好的镜像启动一个容器，请运行：

```bash
x11docker -m sribd-dbeaver-ce
```

x11docker 的更详细介绍和使用方法，请参考其[文档](https://github.com/mviereck/x11docker/wiki)．此镜像内置数据库驱动文件，但仍需用户在启动之后在 DBeaver 的数据库驱动器管理中从 `/opt/dbeaver/drivers` 目录添加．
