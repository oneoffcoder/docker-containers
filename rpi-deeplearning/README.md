# Purpose

The purpose of this container is to create a Python 3.4 Deep Learning environment with Jupyter Lab for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/rpi-deeplearning)

# Tensorflow

Before you may build this docker image, you will need to [cross compile Tensorflow for the Raspberry Pi](https://www.tensorflow.org/install/source_rpi). Note 

* that Tensorflow for Raspberry Pi will only work with Python 3.4, and
* when you compile Tensorflow, you have to compile on a x86 computer (not on a Raspberry Pi or any ARMv7 CPU).

```bash
git clone https://github.com/tensorflow/tensorflow.git

cd tensorflow

git checkout r1.14

CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/usr/include/python3.4" \
    tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
```

After you are done, place the `$TENSORFLOW/output-artifacts` into this directory, where `$TENSORFLOW` is the path to where you checked out the Tensorflow git repository.

# Docker

Build it.

```bash
./build.sh
```

Run it (plain).

```bash
docker run -it -p 8888:8888 rpi-deeplearning:local
```

Run it (with host mount).

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-nlp/ipynb:/ipynb \
    rpi-deeplearning:local
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-nlp/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    rpi-deeplearning:local
```

Observe it.

* [http://localhost:8888](http://localhost:8888)

# Take a Look!

Check out [Martin Odersky](https://en.wikipedia.org/wiki/Martin_Odersky).

# Citation

```
@misc{oneoffcoder_rpi_deeplearning_2019, 
title={Docker container with Tensorflow for Raspberry Pi 4}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/rpi-deeplearning}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jul}}
```
