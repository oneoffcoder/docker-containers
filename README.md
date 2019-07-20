# Intro

These are some sample docker containers for learning purposes.

* [conda-deeplearning](conda-deeplearning): A [container](https://hub.docker.com/r/vangjee/conda-deeplearning) with conda environment + Jupyter for Deep Learning.
* [conda-nlp](conda-nlp): A [container](https://hub.docker.com/r/vangjee/conda-nlp) with conda environment + Jupyter for Natural Language Processing (NLP).
* [nginx-env](nginx-env): A [container](https://hub.docker.com/r/vangjee/nginx-env) showing how to acquire environment variables at runtime for application configuration (externalizing properties).
* [nginx-port](nginx-port): A [container](https://hub.docker.com/r/vangjee/nginx-port) showing how to run nginx on a port specified at runtime through an environment variable.
* [nginx-wsgi](nginx-wsgi): A [container](https://hub.docker.com/r/vangjee/nginx-wsgi) showing how to run flask behind gunicor and nginx.

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
@misc{vang_2019, 
title={Docker Containers}, 
url={https://github.com/vangj/docker-containers}, 
journal={GitHub},
author={Vang, Jee}, 
year={2019}, 
month={Jul}}
```

# Copyright Stuff

```
Copyright 2019 Jee Vang

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