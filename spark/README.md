# Purpose

This docker container is meant to be used for learning purpose for programming Spark. It has the following components.

* Hadoop v3.3.1
* Spark v3.1.2
* Python v3.8

After running the container, you may visit the following pages.

* [HDFS](http://172.18.0.5:9870)
* [Node Manager](http://172.18.0.5:8042)
* [YARN](http://172.18.0.5:8088)
* [Job History](http://172.18.0.5:19888)
* [Spark](http://172.18.0.5:8080)
* [Spark Jobs](http://172.18.0.5:4040)
* [Spark History](http://172.18.0.5:18080)

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
- `8020` : Name Node metadata service
- `8042` : Node Manager
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
# spark standalone
spark-submit \
    --master spark://172.18.0.5:7077 \
    dummy.py

# YARN
HADOOP_CONF_DIR=/home/super/dev/hadoop/etc/hadoop/ spark-submit \
    --deploy-mode client \
    --master yarn dummy.py
```

# References

- [How to resolve pickle error in pyspark?](https://www.py4u.net/discuss/254317?utm_source=pocket_mylist)
- [What can be pickled and unpickled](https://docs.python.org/3.5/library/pickle.html#what-can-be-pickled-and-unpickled)
- [cloudpickle](https://github.com/apache/spark/blob/33ae7a35daa86c34f1f9f72f997e0c2d4cd8abec/python/pyspark/cloudpickle.py)
- [How do I call pyspark code with .whl file?](https://stackoverflow.com/questions/64503039/how-do-i-call-pyspark-code-with-whl-file)
- [Does spark standalone cluster supports deploye mode = cluster for python applications?](https://stackoverflow.com/questions/41919295/does-spark-standalone-cluster-supports-deploye-mode-cluster-for-python-applica)
- [Understand the default configuration](https://docs.bitnami.com/aws/apps/hadoop/get-started/understand-default-config/)
- [Call From kv.local/172.20.12.168 to localhost:8020 failed on connection exception, when using tera gen](https://stackoverflow.com/questions/44304138/call-from-kv-local-172-20-12-168-to-localhost8020-failed-on-connection-exceptio)
- [Yarn JobHistory Error: Failed redirect for container_1400260444475_3309_01_000001](https://stackoverflow.com/questions/24076192/yarn-jobhistory-error-failed-redirect-for-container-1400260444475-3309-01-00000)