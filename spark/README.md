# Purpose

This docker container is meant to be used for learning purpose for programming Spark. It has the following components.

* Hadoop v3.3.1
* Spark v3.1.2
* Python v3.8

After running the container, you may visit the following pages.

* [HDFS](http://172.18.0.5:9870)
* [Node Manager](http://172.18.0.5:8042)
* [YARN](http://172.18.0.5:8088)
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








tcp        0      0 0.0.0.0:13562           0.0.0.0:*               LISTEN      862/java            
tcp        0      0 0.0.0.0:8030            0.0.0.0:*               LISTEN      743/java            
tcp        0      0 0.0.0.0:8031            0.0.0.0:*               LISTEN      743/java            
tcp        0      0 0.0.0.0:18080           0.0.0.0:*               LISTEN      1755/java           
tcp        0      0 0.0.0.0:8032            0.0.0.0:*               LISTEN      743/java            
tcp        0      0 0.0.0.0:8033            0.0.0.0:*               LISTEN      743/java            
tcp        0      0 127.0.0.11:35265        0.0.0.0:*               LISTEN      -                   
tcp        0      0 172.18.0.5:7077         0.0.0.0:*               LISTEN      1221/java           
tcp        0      0 172.18.0.5:41831        0.0.0.0:*               LISTEN      1411/java           
tcp        0      0 0.0.0.0:8040            0.0.0.0:*               LISTEN      862/java            
tcp        0      0 0.0.0.0:9864            0.0.0.0:*               LISTEN      327/java            
tcp        0      0 0.0.0.0:8042            0.0.0.0:*               LISTEN      862/java            
tcp        0      0 0.0.0.0:9866            0.0.0.0:*               LISTEN      327/java            
tcp        0      0 172.18.0.5:46699        0.0.0.0:*               LISTEN      1669/java           
tcp        0      0 172.18.0.5:40139        0.0.0.0:*               LISTEN      1583/java           
tcp        0      0 172.18.0.5:43083        0.0.0.0:*               LISTEN      1497/java           
tcp        0      0 0.0.0.0:9867            0.0.0.0:*               LISTEN      327/java            
tcp        0      0 0.0.0.0:9868            0.0.0.0:*               LISTEN      515/java            
tcp        0      0 0.0.0.0:9870            0.0.0.0:*               LISTEN      165/java            
tcp        0      0 172.18.0.5:38351        0.0.0.0:*               LISTEN      1325/java           
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      1221/java           
tcp        0      0 0.0.0.0:8081            0.0.0.0:*               LISTEN      1325/java           
tcp        0      0 0.0.0.0:8082            0.0.0.0:*               LISTEN      1411/java           
tcp        0      0 0.0.0.0:8083            0.0.0.0:*               LISTEN      1497/java           
tcp        0      0 0.0.0.0:8084            0.0.0.0:*               LISTEN      1583/java           
tcp        0      0 127.0.0.1:8020          0.0.0.0:*               LISTEN      165/java            
tcp        0      0 0.0.0.0:8085            0.0.0.0:*               LISTEN      1669/java           
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      20/sshd: /usr/sbin/ 
tcp        0      0 0.0.0.0:43607           0.0.0.0:*               LISTEN      862/java            
tcp        0      0 0.0.0.0:8088            0.0.0.0:*               LISTEN      743/java            
tcp        0      0 127.0.0.1:35001         0.0.0.0:*               LISTEN      327/java            
tcp6       0      0 :::22                   :::*                    LISTEN      20/sshd: /usr/sbin/