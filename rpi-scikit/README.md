# Purpose

The purpose of this container is to create a Python 3.7 environment with Scikit-Learn + Jupyter Lab for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4.

# Docker Hub

[Image](https://hub.docker.com/r/vangjee/rpi-scikit)

# Docker

Build it.

```bash
./build.sh
```

Run it (plain).

```bash
docker run -it -p 8888:8888 rpi-scikit:local
```

Run it (with host mount).

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-scikit/ipynb:/ipynb \
    rpi-nlp:local
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-scikit/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    rpi-scikit:local
```

Observe it.

* [http://localhost:8888](http://localhost:8888)

# Take a Look!

Check out [George Dantzig](https://en.wikipedia.org/wiki/George_Dantzig).

# Citation

```
@misc{vang_rpi_scikit_2019, 
title={Docker container with Python 3.7 + Jupyter Lab + Scikit-Learn for Raspberry Pi 4},
url={https://github.com/vangj/docker-containers/tree/master/rpi-scikit}, 
journal={GitHub},
author={Vang, Jee},
year={2019},
month={Jul}}
```
