# Purpose

A container demonstrating how to run a Flask application behind gunicorn and nginx.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/nginx-wsgi)

# Docker

Pull it.

```bash
docker pull oneoffcoder/nginx-wsgi:latest
```

Run it.

```bash
docker run -it -p 80:80 --rm oneoffcoder/nginx-wsgi
```

Observe it.
* [http://localhost:80](http://localhost:80)
* [http://localhost:80/v1/test](http://localhost:80/v1/test)