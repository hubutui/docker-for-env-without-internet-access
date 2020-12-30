这个例子构建一个包含 CUDA 的 Miniconda3 镜像．要构建镜像，请运行：

```bash
docker build -t miniconda-cuda:1.0 .
```

这里默认指定构建用的 CUDA 基础镜像的标签为 `10.2-runtime-ubuntu18.04`，以及 Miniconda 的下载链接．用户可以根据需要修改，例如：

```bash
docker build -t miniconda-cuda:1.1 --build-arg CUDA_TAG=10.2-devel-ubuntu18.04 --build-arg URL=https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.8.2-Linux-x86_64.sh .
```

**注意：**需要使用 NVCC 的用户应当使用标签中带 `devel` 的 CUDA 基础镜像．