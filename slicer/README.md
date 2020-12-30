此 Dockerfile 可用于构建 [3D Slicer](https://slicer.org)．要构建此镜像，请运行：

```bash
docker build -t slicer:4.11.20200930 .
```

运行此镜像需要宿主机安装有 [x11docker](https://github.com/mviereck/x11docker) 及其依赖．也可以使用 Singularity 容器技术．

使用 x11docker 从构建好的 Docker 镜像运行一个容器，请使用命令：

```bash
x11docker -m slicer:4.11.20200930
```

使用 Singularity 运行容器需要先将 Docker 镜像转换为 Singularity 镜像：

```bash
sudo singularity build slicer-4.11.20200930.sif docker-daemon://slicer:4.11.20200930
```

然后启动容器：

```bash
singularity run slicer-4.11.20200930.sif
# 或者
singularity run --nv slicer-4.11.20200930.sif
```
