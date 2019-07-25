# Purpose

The purpose of this container is to create a Python 3.7 environment with Natural Language Processing (NLP) APIs for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/rpi-nlp)

# Docker

Pull it.

```bash
docker pull oneoffcoder/rpi-nlp:latest
```

Run it (plain).

```bash
docker run -it -p 8888:8888 oneoffcoder/rpi-nlp
```

Run it (with host mount).

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/docker-containers/rpi-nlp/ipynb:/ipynb \
    oneoffcoder/rpi-nlp
```

Run it (with Jupyter Notebook instead of Jupyter lab)

```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/docker-containers/rpi-nlp/ipynb:/ipynb \
    -e JUPYTER_TYPE=notebook \
    oneoffcoder/rpi-nlp
```

Observe it.

* [http://localhost:8888](http://localhost:8888)
