这个例子构建了一个基于 pytorch 的 [NVIDIA apex](https://github.com/NVIDIA/apex) 的镜像．要构建此镜像，请运行：

```bash
docker build -t nvidia-apex .
```

注意，这里我们用了多阶段构建，在 `pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel` 中编译 apex，然后复制编译结果到 `pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime` 中，得到最后的镜像，从而构建出来更小的镜像文件．