![One-Off Coder Logo](../logo.png "One-Off Coder")

# Notes

To run the container.

```bash
docker run -it \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 8888:8888 \
    -p 9864:9864 \
    -v $HOME/git/docker-containers/spark-jupyter/ubuntu/root/ipynb:/root/ipynb \
    spark-jupyter:local
```

Stuff to do after going into the container e.g. `docker exec -it <id> /bin/bash`

```bash
# test yarn
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar pi 1 50

# test spark against yarn
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

# test spark standalone
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master spark://localhost:7077 \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

# start a scala spark shell
$SPARK_HOME/bin/spark-shell --master spark://localhost:7077

# start a python spark shell
pyspark --master spark://localhost:7077 > /tmp/jupyter.log 2>&1 &

# start a python spark shell against yarn
pyspark \
    --driver-memory 2g \
    --executor-memory 2g \
    --num-executors 1 \
    --executor-cores 1 \
    --conf spark.driver.maxResultSize=8g \
    --conf spark.network.timeout=2000 \
    --queue default \
    --master yarn-client > /tmp/jupyter.log 2>&1 &
```

# Sites

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark History](http://localhost:18080)
* [Jupyter Lab](http://localhost:8888)

# References

* [List of all ports](https://kontext.tech/docs/DataAndBusinessIntelligence/p/default-ports-used-by-hadoop-services-hdfs-mapreduce-yarn)
* [Enable CORS for WebHDFS](https://stackoverflow.com/questions/52768514/how-to-enable-cors-origin-allow-in-webhdfs-hdfs-hadoop-origin-http-local)
* [core-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-project-dist/hadoop-common/core-default.xml)
* [hdfs-default.xml](http://hadoop.apache.org/docs/r3.2.1/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
* [yarn-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
* [mapred-default.xml](https://hadoop.apache.org/docs/r3.2.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
* [Keep docker container running after services start](https://stackoverflow.com/questions/25775266/how-to-keep-docker-container-running-after-starting-services)