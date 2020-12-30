此镜像基于 [consol/ubuntu-xfce-vnc](https://github.com/ConSol/docker-headless-vnc-container/) 改写而来，原文档见[此处](./README.en.md)．它提供了一个 XFCE 桌面环境，并额外添加了 WPS，同时增加了 [stata](https://www.stata.com) 的相关依赖包．可以使用 VNC 客户端登录，或者通过浏览器登录．
要构建此镜像，请运行命令：

```bash
docker build -t stata-debian-xfce-vnc . --progress plain \
    --build-arg NO_VNC_VERSION=1.2.0 \
    --build-arg WEBSOCKIFY_VERSION=0.9.0 \
    --build-arg TIGERVNC_VERSION=1.9.0
```

可根据需要指定 [noVNC](https://github.com/novnc/noVNC)，[Websockify](https://github.com/novnc/websockify) 和 [TigerVNC](https://tigervnc.org/) 的版本．

启动镜像，并挂载目录：

```bash
docker run -d -p \
    5901:5901 -p 6901:6901 \
    --env VNC_PW=yourvncpasswd \
    --user $(id -u):$(id -g) \
    --name $(whoami)-desktop \
    -v /my-stata-install-dir:/usr/local/stata16 \
    -v /my-data-dir-in-host:/data-dir-in-container \
    stata-debian-xfce-vnc
```

这里我们需要提前在本地的一台 Linux 机器上安装、激活和更新好 stata，然后将整个 stata 安装目录打包上传，运行时将其挂载到容器内的 `/usr/local/stata16` 目录．
注意启动 Docker 容器后查看端口映射到宿主机的端口是否空闲，若被占用需更换合适的端口．

## 基于此镜像修改

需要在此镜像上添加自己的软件包的，应该直接修改 Dockerfile，把安装其他软件包和依赖的指令写到 `CMD` 指令之前．不建议直接使用 `stata-debian-xfce-vnc`，会有意想不到的麻烦．
此例子适合类似 stata 这种解压即可使用的第三方或者闭源软件，只需在镜像内安装其依赖包，运行时将改软件的安装目录挂载到容器内即可使用．