这个例子构建了一个 R 语言环境的镜像．它用的是 Miniconda3 作为基础镜像．如果以此为基础定制自己的镜像，我们建议首先使用 `conda` 命令从 `r`，`conda-forge` 和 `bioconda` 等 channel 安装所需的 R 语言包，其次再考虑使用 R 语言的 `install.packages` 函数从 CRAN 安装其他包，以及使用 `devtools::install_github` 从 Github 安装包．使用 `install.packages` 函数来安装 R 语言包的方法请参考本项目中的另外一个[例子](../r-base)．

要构建此镜像，请运行：

```bash
docker build -t sribd-r:3.6.1 .
```

同样地，用户可以根据需要指定 `--build-arg` 选项来设置 Dockerfile 中的 `ARG`．例如，构建 R 4.0.1 版本：

```bash
docker build -t sribd-r:4.0.1 --build-arg R_VERSION=4.0.1 .
```

**注意：**此镜像不含 CUDA．