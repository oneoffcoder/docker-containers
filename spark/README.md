# Purpose

This docker container is meant to be used for learning purpose for programming Spark. It has the following components.

* Hadoop v3.3.1
* Spark v3.1.2
* Python v3.8

After running the container, you may visit the following pages.

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark Jobs](http://localhost:4040)
* [Spark History](http://localhost:18080)

# Docker

Build.

```bash
./build.sh
```

Run.

```bash
./run.sh
```

# Ports

[Hadoop](https://docs.bitnami.com/aws/apps/hadoop/get-started/understand-default-config/)

- `9870` : Name Node (HDFS)
- `8088` : Resource Manager (YARN)
- `9864` : Data node
- `19888` : History Server

[Spark](https://www.ibm.com/docs/en/zpfas/1.1.0?topic=spark-configuring-networking-apache)

- `8080` : Master web UI
- `18080` : History server web UI
- `7077` : Master port
- `4040` : Application web UI

# Test Connection

```bash
./bin/spark-shell \
    --master spark://localhost:7077 \
    --conf spark.ui.port=4041
```