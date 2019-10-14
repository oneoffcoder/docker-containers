![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

The purpose of this container is to create a Deep Learning [Conda](https://anaconda.org/) environment with Jupyter Lab.

Here are some Deep Learning packages installed.

* [TensorFlow](https://www.tensorflow.org/)
* [PyTorch](https://pytorch.org/)
* [MXNet](https://mxnet.apache.org/)
* [spaCy](https://spacy.io)
* [AllenNLP](https://allennlp.org)

Note that this container requires [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker) (look at the `runtime=nvidia` requirement below when running this container). You will also need [CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive), [cuDNN 7](https://developer.nvidia.com/cudnn), and [NCCL 2.3](https://developer.nvidia.com/nccl) installed on your host computer.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/conda-deeplearning)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -p 8888:8888 \
    conda-deeplearning:local
```

Run it with a mounted host folder.

```bash
docker run -it \
    -v $HOME/git/docker-containers/conda-deeplearning/ipynb:/ipynb \
    -p 8888:8888 \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    conda-deeplearning:local
```

Observe it.

* [http://localhost:8888](http://localhost:8888)

# Links

* [GitHub NVIDIA Docker](https://github.com/NVIDIA/nvidia-docker)
* [NVIDIA CUDA docker image](https://hub.docker.com/r/nvidia/cuda)
* [Anaconda Install Scripts](https://repo.anaconda.com/archive/)
* [Install Anaconda in silent mode](https://docs.anaconda.com/anaconda/install/silent-mode/)
* [Include .whl installation in requirements.txt](https://stackoverflow.com/questions/45018492/include-whl-installation-in-requirements-txt)
* [Tensorflow Install GPU](https://www.tensorflow.org/install/gpu)

# Take a Look!

Check out [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church).

# Citation

```
@misc{oneoffcoder_conda_deeplearning_2019, 
title={Docker container for Deep Learning with Jupyter Lab}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/conda-deeplearning}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jul}}
```
