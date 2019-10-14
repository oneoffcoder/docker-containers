![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

This container shows how to build a container that may be used as a executable. The [idea](https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/) is to use the `ENTRYPOINT` and `CMD` instructions together. The `ENTRYPOINT` instruction points to the program and the `CMD` instruction may be used to capture arguments passed into the docker container at runtime to pass to the program (pointed to by `ENTRYPOINT`). In this example, we have a simple Python program that takes in the first, middle and last name and prints `hello, first_name middle_name last_name!` back to the console.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/docker-exe)

# Docker

Build it.

```bash
./build.sh
```

Run it.

Observe it.

```bash
docker run -it docker-exe:local -f Donald -m John -l Trump
```

# Take a Look!

Check out [Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace).

# Citation

```
@misc{oneoffcoder_docker_exe_2019, 
title={Showing how to create a container that may be used as an executable}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/docker-exe}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Aug}}
```