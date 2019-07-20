# Purpose

The purpose of this project is to demonstrate the ability to run [nginx](https://www.nginx.com/), [gunicorn](https://gunicorn.org/) and [flask](http://flask.pocoo.org/) together in a Docker container. 

## Why is this demonstration even important?

### Robust deployment

In any case of deployment (especially production deployment), using flask alone to serve request is not the right thing to do. Typically, gunicorn is placed in front of flask to receive the request; gunicorn helps out primarily by scaling out the flask service (see [here](https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7) and [here](https://ironboundsoftware.com/blog/2016/06/27/faster-flask-need-gunicorn/)). Additionally, gunicorn itself is inadequate and nginx comes into play for [better performance](https://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn) such as serving dynamic or static content; in the case of dynamic content, nginx will delegate this to gunicorn; in the case of static content, nginx will do better at serving those content back. There are many reported performance problems with using flask alone, and this demonstration shows a template containerized approach you may adapt to properly deploy your flask application.

### Multiple services
One complication comes with having `nginx` and `gnunicorn` that have to both run at container startup. In Docker, you can only have one `CMD` command. Thus, you can only run either `nginx` or `gnunicorn`. 

```bash
CMD ["gunicorn", "-b", "unix:app.sock ", "-w", "4", "--chdir", "/app", "app:app"]
```

or

```bash
CMD ["nginx", "-g", "daemon off;"]
```

You can [use](https://unix.stackexchange.com/questions/37069/what-is-the-difference-between-and-when-chaining-commands) the single `CMD` with `&&` or `;` to start both services. However, that seems a bit undisciplined as these are services, and also, take a look at how the array passed to `CMD` grows. (I'm not even sure if the following will work; besides, which service will be in the foreground and which in the background?).

```bash
CMD ["gunicorn", "-b", "unix:app.sock ", "-w", "4", "--chdir", "/app", "app:app", ";", "nginx", "-g", "daemon off;"]
```

The best approach is to use [supervisor](http://supervisord.org/) to control the services. What I like about `supervisor` is that it is easy to configure and it can restart failed services. Futhermore, both services are now in the foreground (you are able to monitor logging to the console for debugging purpose).

# Docker Hub

[Image](https://hub.docker.com/r/vangjee/nginx-wsgi)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it -p 80:80 --rm nginx-wsgi:local
```

Observe it.

* [http://localhost](http://localhost)

# References

* [Using Supervisor with Docker to manage processes](https://blog.trifork.com/2014/03/11/using-supervisor-with-docker-to-manage-processes-supporting-image-inheritance/)
* [Why can't I use Docker CMD multiple times to run multiple services?
](https://stackoverflow.com/questions/23692470/why-cant-i-use-docker-cmd-multiple-times-to-run-multiple-services)
* [Docker Alpine linux running 2 programs](https://stackoverflow.com/questions/49090469/docker-alpine-linux-running-2-programs)
* [/etc/nginx/proxy_params failed (2: No such file or directory)](https://stackoverflow.com/questions/42589781/django-nginx-emerg-open-etc-nginx-proxy-params-failed-2-no-such-file)

# Take a Look!

Check out [John Papa](https://johnpapa.net/). He's got some good philosophical approaches to creating awesome software.

# Citation

```
@misc{vang_nginx_gunicorn_flask_demo_2019, 
title={HOWTO create a docker container with nginx, gunicorn and flask}, 
url={https://github.com/vangj/docker-containers/tree/master/nginx-wsgi}, 
journal={GitHub},
author={Vang, Jee}, 
year={2019}, 
month={Jun}}
```

# Copyright Stuff

```
Copyright 2019 Jee Vang

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
