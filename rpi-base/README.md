# Purpose

The purpose of this container is to create a base Docker image for use with Raspberry Pi 4 (armv7l).

Note that you should be building and using this container only on a Raspberry Pi 4. If you want to build this container on an x86 machine, try [this approach](https://blog.hypriot.com/post/docker-intel-runs-arm-containers/).

```bash
docker run --rm --privileged hypriot/qemu-register
```

# Docker Hub

[Image](https://hub.docker.com/r/vangjee/rpi-base)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it rpi-base:local
```

Observe it.

```bash
docker run -it rpi-base:local
```

# Take a Look!

Check out [X](https://X).

# Citation

```
@misc{vang_rpi_base_2019, 
title={Base Docker container Raspberry Pi 4}, 
url={https://github.com/vangj/docker-containers/tree/master/rpi-base}, 
journal={GitHub},
author={Vang, Jee}, 
year={2019}, 
month={Jul}}
```
