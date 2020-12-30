这个例子构建了一个 R 语言环境的镜像．它用的是 Miniconda3 作为基础镜像．更加完整的例子请看[这里](../r)．

要构建此镜像，请运行：

```bash
docker build -t r-miniconda:1.0 .
```

同样地，用户可以根据需要指定 `--build-arg` 选项来设置 Dockerfile 中的 `ARG`．

**注意：**此镜像不含 CUDA．