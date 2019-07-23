# Purpose

A container demonstrating how to run nginx on a port passed in from an environment variable.

# Source

[GitHub](https://github.com/vangj/docker-containers/tree/master/nginx-port)

# Docker

Pull it.

```bash
docker pull vangjee/nginx-port:latest
```

Run it.

```bash
docker run -p 81:81 -e PORT=81 --rm vangjee/nginx-port
docker run -p 82:82 -e PORT=82 --rm vangjee/nginx-port
docker run -p 83:83 -e PORT=83 --rm vangjee/nginx-port
```

Observe it. 

* [http://localhost:81](http://localhost:81)
* [http://localhost:82](http://localhost:82)
* [http://localhost:83](http://localhost:83)