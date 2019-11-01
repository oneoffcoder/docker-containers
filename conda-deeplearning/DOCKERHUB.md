# Purpose

The purpose of this container is to create a Deep Learning [Conda](https://anaconda.org/) environment with Jupyter Lab.

Here are some Deep Learning packages installed.

* [TensorFlow](https://www.tensorflow.org/)
* [PyTorch](https://pytorch.org/)
* [MXNet](https://mxnet.apache.org/)
* [spaCy](https://spacy.io)
* [AllenNLP](https://allennlp.org)

Note that this container requires [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker) (look at the `runtime=nvidia` requirement below when running this container). You will also need [CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive), [cuDNN 7](https://developer.nvidia.com/cudnn), and [NCCL 2.3](https://developer.nvidia.com/nccl) installed on your host computer.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/conda-deeplearning)

# Docker

Pull it.

```bash
docker pull oneoffcoder/conda-deeplearning:latest
```

Run it.

```bash
docker run -it \
    --shm-size=5g \
    -gpus all \
    -p 8888:8888 \
    oneoffcoder/conda-deeplearning
```

Run it with a mounted host folder.

```bash
docker run -it \
    -v $HOME/git/docker-containers/conda-deeplearning/ipynb:/ipynb \
    -p 8888:8888 \
    --shm-size=5g \
    -gpus all \
    oneoffcoder/conda-deeplearning
```

Use it.

* [http://localhost:8888](http://localhost:8888)
