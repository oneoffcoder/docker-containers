# Purpose

The purpose of this container is to demonstrate how to read environment variables and write them to a directory. When deploying a container application (e.g. Angular application), at runtime, you might have to read environment variables to configure the application.

This container uses [supervisor](http://supervisord.org/) to achieve the intended effect as an attempt to be a disciplined approach. For example, you could create a shell script and use `ENTRYPOINT` or `CMD` to execute that shell script at startup. However, how would you put multiple services into the foreground? In this container, supervisor calls the `doit.sh` script to read the environment variables, and then writes them to `/usr/share/nginx/html/env.json`; the service is called `setupenv`. Finally, the supervisor service called `nginx` starts nginx in non-daemon mode.

# Docker Hub

[Image](https://cloud.docker.com/repository/docker/vangjee/nginx-env)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it -p 80:80 nginx-env:local
```

Observe it.

```bash
docker exec -it [CONTAINER_ID] cat /usr/share/nginx/html/env.json
docker exec -it [CONTAINER_ID] /bin/bash
```
