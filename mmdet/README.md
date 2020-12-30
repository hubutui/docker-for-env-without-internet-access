这个例子构建了一个基于 pytorch 的 [mmdetection](https://github.com/open-mmlab/mmdetection) 的镜像．要构建此镜像，请运行：

```bash
docker build -t mmdet:2.3.1 .
```

注意，这里我们用了 `pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime` 作为基础镜像，它不包含 NVCC．因为构建步骤中没有需要用到 NVCC 来编译的．构建出来的镜像文件更小．