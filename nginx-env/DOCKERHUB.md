# Purpose

An nginx container showing how to acquire and save environment variables at runtime (useful for Kubernetes and deployment of single page application frameworks like Angular).

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/nginx-env)

# Docker

Pull it.

```bash
docker pull oneoffcoder/nginx-env:latest
```

Run it.

```bash
docker run -it -p 80:80 oneoffcoder/nginx-env
```

Observe it.

```bash
docker exec -it [CONTAINER_ID] cat /usr/share/nginx/html/env.json
```