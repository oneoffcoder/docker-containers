# Purpose

The purpose of this container is to create a Python 3.7 environment with Jupyter Lab (and Notebook) for use with Raspberry Pi 4 (armv7l).

# Source

[GitHub](https://github.com/vangj/docker-containers/tree/master/rpi-jupyterlab)

# Docker

Pull it.

```bash
docker pull vangjee/rpi-jupyterlab:latest
```

Run it (plain).

```bash
docker run -it -p 8888:8888 vangjee/rpi-jupyterlab
```

Run it (with host mount).

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-jupyterlab/ipynb:/ipynb \
    vangjee/rpi-jupyterlab
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v /home/pi/git/docker-containers/rpi-jupyterlab/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    vangjee/rpi-jupyterlab
```

Observe it.

* [http://localhost:8888](http://localhost:8888)