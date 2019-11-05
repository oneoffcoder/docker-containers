![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

The purpose of this container is to create a Deep Learning [Conda](https://anaconda.org/) environment with Jupyter Lab.

Here are some Deep Learning packages installed.

* [TensorFlow](https://www.tensorflow.org/) v2.0
* [PyTorch](https://pytorch.org/) v1.3
* [MXNet](https://mxnet.apache.org/)
* [spaCy](https://spacy.io)
* [AllenNLP](https://allennlp.org)

Note that this container requires [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker). You will also need [CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive), [cuDNN 7](https://developer.nvidia.com/cudnn), and [NCCL 2.3](https://developer.nvidia.com/nccl) installed on your host computer.

## Ubuntu
On Ubuntu 19+, `nvidia-docker2` is not yet published. You need to do the following.

```bash
distribution=ubuntu18.04
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
 
# check runtime hook is installed
which nvidia-container-runtime-hook
 
# make sure container detects gpu
docker run --gpus all --rm nvidia/cuda nvidia-smi
```

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
    --shm-size=5g \
    --gpus all \
    -p 8888:8888 \
    conda-deeplearning:local
```

Run it with a mounted host folder.

```bash
docker run -it \
    -v $HOME/git/docker-containers/conda-deeplearning/ipynb:/root/ipynb \
    -p 8888:8888 \
    --shm-size=5g \
    --gpus all \
    conda-deeplearning:local
```

Run it with password protection.

```bash
docker run -it \
    -v $HOME/git/docker-containers/conda-deeplearning/ipynb:/root/ipynb \
    -p 8888:8888 \
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
    --shm-size=5g \
    --gpus all \
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
