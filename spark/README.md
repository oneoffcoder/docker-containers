# Purpose

This docker container is meant to be used for learning purpose for programming PySpark. It has the following components.

* Hadoop v3.3.1
* Spark v3.1.2
* Python v3.8

After running the container, you may visit the following pages.

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark History](http://localhost:18080)

# Docker

Build.

```bash
docker build --no-cache -t spark0:local -f Dockerfile.stage0 .
docker build --no-cache -t spark:local -f Dockerfile.stage1 .
```

Run.

```bash
docker run --rm -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 8888:8888 \
    -p 9864:9864 \
    -e SPARK_WORKER_INSTANCES="5" \
    -e SPARK_WORKER_CORES="2" \
    -e SPARK_WORKER_MEMORY="5g" \
    spark:local
```