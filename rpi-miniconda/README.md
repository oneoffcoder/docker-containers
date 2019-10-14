![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

The purpose of this container is to create a Miniconda environment for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4. If you want to build this container on an x86 machine, try [this approach](https://blog.hypriot.com/post/docker-intel-runs-arm-containers/).

```bash
docker run --rm --privileged hypriot/qemu-register
```

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/rpi-miniconda)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it rpi-miniconda:local
```

Observe it.

```bash
docker run -it rpi-miniconda:local
```

# Links

* https://stackoverflow.com/questions/39371772/how-to-install-anaconda-on-raspberry-pi-3-model-b
* https://stackoverflow.com/questions/49338902/how-to-install-anaconda-miniconda-on-linux-silently

# Take a Look!

Check out [James Gosling](https://en.wikipedia.org/wiki/James_Gosling).

# Citation

```
@misc{oneoffcoder_rpi_miniconda_2019, 
title={Docker container with Miniconda for Raspberry Pi 4}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/rpi-miniconda}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jul}}
```
