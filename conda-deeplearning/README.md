# Purpose

The purpose of this container is to create a Deep Learning [Conda](https://anaconda.org/) environment.

Here are some Deep Learning packages installed.

* [TensorFlow](https://www.tensorflow.org/)
* [PyTorch](https://pytorch.org/)
* [MXNet](https://mxnet.apache.org/)
* [spaCy](https://spacy.io)
* [AllenNLP](https://allennlp.org)

Note that this container requires [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker) (look at the `runtime=nvidia` requirement below when running this container).

# Docker Hub

[Image](https://cloud.docker.com/repository/docker/vangjee/conda-deeplearning)

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
    -v /home/super/git/docker-containers/conda-deeplearning/ipynb:/ipynb \
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