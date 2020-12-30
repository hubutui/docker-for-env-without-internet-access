这个例子同样构建了一个包含 CUDA 的 Miniconda3 镜像，但是与本项目中的另外一个[例子](../miniconda-cuda)不同的是，它用了多阶段构建．要构建此镜像，请运行命令：

```bash
docker build -t miniconda-cuda:2.0 .
```

同样地，你也可以使用 `--build-arg` 来设定 Dockerfile 中的 `ARG`．例如：

```bash
docker build -t miniconda-cuda:2.1 --build-arg CUDA_TAG=10.2-devel-ubuntu18.04 --build-arg MINICONDA_VERSION=4.9.2 .
```

**注意：**需要使用 NVCC 的用户应当使用标签中带 `devel` 的 CUDA 基础镜像．