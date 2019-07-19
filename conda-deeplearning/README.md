# Purpose

The purpose of this container is to create a Deep Learning [Conda](https://anaconda.org/) environment.

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it -p 8888:8888 conda-deeplearning:local
```

Run it with a mounted host folder.

```bash
docker run -it -v /home/user/ipynb:/ipynb -p 8888:8888 conda-deeplearning:local
```

Observe it: [http://localhost:8888](http://localhost:8888).
