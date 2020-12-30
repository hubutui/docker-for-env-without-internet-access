这个例子直接使用 Docker 官方提供的 r-base 镜像作为基础，然后在上面使用 R 语言的 `install.packages` 函数来安装所需的 R 语言包．这里，我们把安装 R 语言包的 R 代码写到了脚本 `requirements.R` 中，然后在构建镜像的时候将这个脚本复制到容器内，使用 `Rscript` 命令去运行该脚本，执行实际的 R 包的安装．要构建镜像，请运行：

```bash
docker build -t sribd-r-base:1.0
```