# Purpose

The purpose of this container is to create a Natural Language Processing (NLP) [Conda](https://anaconda.org/) environment.

# Docker

```bash
./build.sh
```

Run it.

```bash
docker run -it -p 8888:8888 conda-nlp:local
```

Run it with a mounted host folder.

```bash
docker run -it -v /home/user/ipynb:/ipynb -p 8888:8888 conda-nlp:local
```

Observe it: [http://localhost:8888](http://localhost:8888).
