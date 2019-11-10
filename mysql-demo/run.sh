#!/bin/bash

docker run \
    -e MYSQL_ROOT_PASSWORD=oneoffcoder \
    --rm mysql-demo:local