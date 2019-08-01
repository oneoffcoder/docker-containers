# Intro

These are some sample docker containers for learning purposes.

* [dl-darknet](dl-dkarnet): [YOLO object detection](https://github.com/pjreddie/darknet) with [darknet](https://github.com/AlexeyAB/darknet) in a [box](https://hub.docker.com/r/oneoffcoder/dl-darknet)!
* [conda-deeplearning](conda-deeplearning): A [container](https://hub.docker.com/r/oneoffcoder/conda-deeplearning) with conda environment + Jupyter for Deep Learning.
* [conda-nlp](conda-nlp): A [container](https://hub.docker.com/r/oneoffcoder/conda-nlp) with conda environment + Jupyter for Natural Language Processing (NLP).
* [nginx-env](nginx-env): A [container](https://hub.docker.com/r/oneoffcoder/nginx-env) showing how to acquire environment variables at runtime for application configuration (externalizing properties).
* [nginx-port](nginx-port): A [container](https://hub.docker.com/r/oneoffcoder/nginx-port) showing how to run nginx on a port specified at runtime through an environment variable.
* [nginx-wsgi](nginx-wsgi): A [container](https://hub.docker.com/r/oneoffcoder/nginx-wsgi) showing how to run flask behind gunicorn and nginx.
* [rpi-python37](rpi-python37): A [container](https://hub.docker.com/r/oneoffcoder/rpi-python37) with Python 3.7 for use with Raspberry Pi 4.
* [rpi-base](rpi-base): A [container](https://hub.docker.com/r/oneoffcoder/rpi-base) for use with Raspberry Pi 4.
* [rpi-miniconda](rpi-miniconda): A [container](https://hub.docker.com/r/oneoffcoder/rpi-miniconda) with Miniconda and Python 3.6 for use with Raspberry Pi 4.
* [rpi-jupyterlab](rpi-jupyterlab): A [container](https://hub.docker.com/r/oneoffcoder/rpi-jupyterlab) with Python 3.6 + Jupyter Lab (and Notebook) for Raspberry Pi 4.
* [rpi-scikit](rpi-scikit): A [container](https://hub.docker.com/r/oneoffcoder/rpi-scikit) with Python 3.6 + Scikit-Learn + Jupyter Lab for Raspberry Pi 4.
* [rpi-nlp](rpi-nlp): A [container](https://hub.docker.com/r/oneoffcoder/rpi-nlp) with Python 3.6 + NLTK + gensim + Stanford Core NLP + textblob + Jupyter Lab for Raspberry Pi 4.
* [rpi-deeplearning](rpi-deeplearning): A [container](https://hub.docker.com/r/oneoffcoder/rpi-deeplearning) with Python 3.6 + Scikit-Learn + NLP + Tensorflow + Jupyter Lab for Raspberry Pi 4.
* [rpi-darknet](rpi-darkent): [YOLO object detection](https://github.com/pjreddie/darknet) with [darknet](https://github.com/AlexeyAB/darknet) in a [box](https://hub.docker.com/r/oneoffcoder/rpi-darknet) for Raspberry Pi 4! Be careful, not for the faint of heart!

# Raspberry Pi Images

Here are the dependencies between the RPi Docker images.

* rpi-base
* rpi-miniconda, rpi-darknet (from rpi-base)
* rpi-jupyterlab (from rpi-miniconda)
* rpi-scikit (from rpi-jupyterlab)
* rpi-nlp (from rpi-scikit)
* rpi-deeplearning (from rpi-nlp)

The rpi-python37 docker image does not depend on the others.

# Docker Hub

The instructions for publishing to Docker Hub are [here](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html).

# Cleaning up

Remove all exited docker images

```bash
docker rm $(docker ps -q -f status=exited)
```

Remove all docker images that are dangling.

```bash
docker image rm $(docker images -f dangling=true -q)
```

Remove stopped container and images without any container associations.

```bash
docker system prune -a -f
```

# Citation

```
@misc{oneoffcoder_docker_containers_2019, 
title={Docker Containers}, 
url={https://github.com/oneoffcoder/docker-containers}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jul}}
```

# Copyright Stuff

```
Copyright 2019 One-Off Coder

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
