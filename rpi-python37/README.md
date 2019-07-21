# Purpose

The purpose of this container is to create a Python 3.7 environment for use with Raspberry Pi 4 (armv7l).

# Docker Hub

[Image](https://hub.docker.com/r/vangjee/rpi-python37)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it rpi-python37:local
```

Observe it.

```bash
docker run -it rpi-python37:local python -c "print('hello, world')"
```

# Take a Look!

Check out [Ross Quinlan](https://en.wikipedia.org/wiki/Ross_Quinlan).

# Citation

```
@misc{vang_rpi_python37_2019, 
title={Docker container with Python 3.7 for Raspberry Pi 4}, 
url={https://github.com/vangj/docker-containers/tree/master/rpi-python37}, 
journal={GitHub},
author={Vang, Jee}, 
year={2019}, 
month={Jul}}
```
