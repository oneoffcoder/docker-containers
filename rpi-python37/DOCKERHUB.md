# Purpose

The purpose of this container is to create a Python 3.7 environment for use with Raspberry Pi 4 (armv7l).

# Source

[GitHub](https://github.com/vangj/docker-containers/tree/master/rpi-python37)

# Docker

Pull it.

```bash
docker pull vangjee/rpi-python37:latest
```

Run it.

```bash
docker run -it vangjee/rpi-python37
```

Observe it.

```bash
docker run -it vangjee/rpi-python37 python3.7 -c "print('hello, world')"
```