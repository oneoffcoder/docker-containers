# Purpose

The purpose of this container is to create a Python 3.4 Deep Learning environment with Jupyter Lab for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/rpi-deeplearning)

# Tensorflow

Before you may build this docker image, you will need to [cross compile Tensorflow for the Raspberry Pi](https://www.tensorflow.org/install/source_rpi). Note when you compile Tensorflow, you have to compile on a x86 computer (not on a Raspberry Pi or any ARMv7 CPU).

```bash
git clone https://github.com/tensorflow/tensorflow.git

cd tensorflow

git checkout r1.14

tensorflow/tools/ci_build/ci_build.sh PI \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE
```

After you are done, place the `$TENSORFLOW/output-artifacts` into this directory, where `$TENSORFLOW` is the path to where you checked out the Tensorflow git repository. Additionally, rename `tensorflow-1.14.1-cp34-none-linux_armv7l.whl` to `tensorflow-1.14.1-cp36-none-linux_armv7l.whl`.

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
    -v $HOME/git/docker-containers/rpi-deeplearning/ipynb:/ipynb \
    rpi-deeplearning:local
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/docker-containers/rpi-deeplearning/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    rpi-deeplearning:local
```

Observe it.

* [http://localhost:8888](http://localhost:8888)

# Links

* https://stackoverflow.com/questions/33622613/tensorflow-installation-error-not-a-supported-wheel-on-this-platform
* https://askubuntu.com/questions/183312/how-are-so-files-used-in-ubuntu

# Take a Look!

Check out [John Backus](https://en.wikipedia.org/wiki/John_Backus).

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
