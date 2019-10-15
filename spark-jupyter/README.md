![One-Off Coder Logo](../logo.png "One-Off Coder")

# Notes

```bash
docker run -it -p 9870:9870 -p 8088:8088 -p 8080:8080 -p 18080:18080 spark-jupyter:local

service ssh start \
    && $HADOOP_HOME/sbin/start-all.sh \
    && $SPARK_HOME/sbin/start-all.sh \
    && $SPARK_HOME/sbin/start-history-server.sh

yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar pi 1 50

$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master spark://localhost:7077 \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

$SPARK_HOME/bin/spark-shell --master spark://localhost:7077

$HADOOP_HOME/sbin/stop-all.sh \
    && $SPARK_HOME/sbin/stop-all.sh \
    && $SPARK_HOME/sbin/stop-history-server.sh
```

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark History](http://localhost:18080)

* https://stackoverflow.com/questions/19641326/http-localhost50070-does-not-work-hadoop