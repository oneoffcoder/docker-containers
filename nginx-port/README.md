# Intro

This project shows `HOWTO` create a Docker container using nginx where the nginx server can `dynamically` acquire values from environment variables passed in by docker (e.g. using the `-e` command).

Before you build the docker image, build the Angular application.

```bash
npm install
ng build
```

Then build the docker image by typing in the following.

```bash
docker build -t nginx-port:local .
```

To test running on different ports, run one of the following.

```bash
docker run -p 81:81 -e PORT=81 --rm nginx-port:local
docker run -p 82:82 -e PORT=82 --rm nginx-port:local
docker run -p 83:83 -e PORT=83 --rm nginx-port:local
```
# Notes

Note the following.
* The Angular application is a vanilla one using the [ng-cli](https://cli.angular.io/) command `ng new`. This application is necessary to show only a toy deployment of a client-side application with nginx as the HTTP server.
* In the `Dockerfile`, we have `CMD ["nginx", "-g", "daemon off;"]` to force nginx to run in the foreground. The `-g` is a `global` setting. This option of turning off daemon mode is useful for debugging and should be turned off for production.
* Note that we are using `envsubst` to acquire the values of the environment variables. This approach is the [recommended way](http://nginx.org/en/docs/ngx_core_module.html#env). Look at the `docker-entrypoint.sh` script. We are using a nginx configuration template `nginx-default.conf.template` to help.
* Elsewhere, people [suggest](https://serverfault.com/questions/577370/how-can-i-use-environment-variables-in-nginx-conf) using [openresty](https://openresty.org/en/). This approach took me down a rabbit hole. Supposedly, openresty can use `lua` and `perl` inside the `nginx.conf` file to acquire environment variables. If you figure out `HOTWO` do this approach successfully, email me. ;)
* This approach might help with Azure's [Linux App Service VNET Integration](https://github.com/Azure/app-service-linux-docs/blob/master/app_service_linux_vnet_integration.md) where they pass in `-e PORT=<some_port>` (`<some_port>` is a random value) to the container. The example they show is with a Node.js Express app which has the `process.env.PORT` API access to environment variables (server-side applications like [flask](http://flask.pocoo.org/) are also able to acquire environment variable values too e.g. `os.getenv('PORT', 80)`). However, with a client-side application like Angular hosted on `nginx`, this approach will help (as Angular will not have those API hooks).

# Take a Look!

Check out [Charles Petzold](https://en.wikipedia.org/wiki/Charles_Petzold). He's my favorite author when it comes to programming books.

# Citation

```
@misc{vang_nginx_env_vars_2019, 
title={nginx with dynamic environment variables}, 
url={https://github.com/vangj/nginx-proj/}, 
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