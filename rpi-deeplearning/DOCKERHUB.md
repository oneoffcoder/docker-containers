# Purpose

The purpose of this container is to create a Python 3.7 environment with Tensorflow v1.14 for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/rpi-deeplearning)

# Docker

Pull it.

```bash
docker pull oneoffcoder/rpi-deeplearning:latest
```

Run it (plain).

```bash
docker run -it -p 8888:8888 oneoffcoder/rpi-deeplearning
```

Run it (with host mount).

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/docker-containers/rpi-deeplearning/ipynb:/ipynb \
    oneoffcoder/rpi-nlp
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/docker-containers/rpi-nlp/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    oneoffcoder/rpi-deeplearning
```

Observe it.

* [http://localhost:8888](http://localhost:8888)
