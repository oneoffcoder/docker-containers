#!/bin/bash

docker run --rm -it \
    --network sparknet \
    --ip 172.18.0.5 \
    -p 9870:9870 \
    -p 8020:8020 \
    -p 8088:8088 \
    -p 9864:9864 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 7077:7077 \
    -e SPARK_WORKER_INSTANCES="5" \
    -e SPARK_WORKER_CORES="2" \
    -e SPARK_WORKER_MEMORY="5g" \
    spark:local