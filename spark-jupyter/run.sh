#!/bin/bash

docker run -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 8888:8888 \
    -p 9864:9864 \
    -e PYSPARK_MASTER=spark://localhost:7077 \
    spark-jupyter:local
