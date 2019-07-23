# Purpose

The purpose of this container is to create a Python 3.7 environment with Jupyter Lab for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4.

# Docker Hub

[Image](https://hub.docker.com/r/vangjee/rpi-jupyterlab)

# Docker

Build it.

```bash
./build.sh
```

Run it (plain).

```bash
docker run -it -p 8888:8888 rpi-jupyterlab:local
```

Run it (with host mount).

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-jupyterlab/ipynb:/ipynb \
    rpi-jupyterlab:local
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-jupyterlab/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    rpi-jupyterlab:local
```

Observe it.

* [http://localhost:8888](http://localhost:8888)

# Take a Look!

Check out [Tom Mitchell](http://www.cs.cmu.edu/~tom/).

# Citation

```
@misc{vang_rpi_jupyterlab_2019, 
title={Docker container with Python 3.7 and Jupyter Lab for Raspberry Pi 4}, 
url={https://github.com/vangj/docker-containers/tree/master/rpi-jupyterlab}, 
journal={GitHub},
author={Vang, Jee}, 
year={2019}, 
month={Jul}}
```
