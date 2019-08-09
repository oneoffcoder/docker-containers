# Purpose

This container shows how to build a container that may be used as a executable. The [idea](https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/) is to use the `ENTRYPOINT` and `CMD` instructions together. The `ENTRYPOINT` instruction points to the program and the `CMD` instruction may be used to capture arguments passed into the docker container at runtime to pass to the program (pointed to by `ENTRYPOINT`). In this example, we have a simple Python program that takes in the first, middle and last name and prints `hello, first_name middle_name last_name!` back to the console.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/docker-exe)

# Docker

Pull it.

```bash
docker pull oneoffcoder/docker-exe:latest
```

Run it.

Observe it.

```bash
docker run -it oneoffcoder/docker-exe -f Donald -m John -l Trump
```
