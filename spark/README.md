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

We need to create a network. The reason is because we cannot specify a static IP for the container if we do NOT use a custom-created network. Why do we need to specify a static IP? Because `SPARK_MASTER_HOST` is typically set to `localhost` and `localhost` binds only to `127.0.0.1` and any request from the outside to the container on port `7077` will be rejected. We can specify for `SPARK_MASTER_HOST` to be `0.0.0.0` explicitly, but, this specification breaks Spark entirely (computations will not run as workers cannot find the master). The workaround is to create a network and assign a static IP to the container.

```bash
docker network create --subnet=172.18.0.0/16 sparknet
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

Some network useful commands.

```bash
docker network ls
docker network inspect sparknet
netstat -tulpn | grep LISTEN
```

If you want to use the shell on the container.

```bash
docker exec -it <CONTAINER_ID> spark-shell --master spark://172.18.0.5:7077
docker exec -it <CONTAINER_ID> pyspark --master spark://172.18.0.5:7077
```

If you want to use a locally installed instance of Spark.

```bash
spark-shell --master spark://172.18.0.5:7077
pyspark --master spark://172.18.0.5:7077
```

If you want to submit an Python application.

```bash
spark-submit \
    --master spark://172.18.0.5:7077 \
    dummy.py
```