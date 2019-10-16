![One-Off Coder Logo](../logo.png "One-Off Coder")

# Notes

```bash
docker run -it -p 9870:9870 -p 8088:8088 -p 8080:8080 -p 18080:18080 -p 9000:9000 -p 8888:8888 spark-jupyter:local

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

export PYSPARK_PYTHON=/user/local/conda/bin/python
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS="lab --port 8888 --notebook-dir='~/' --ip='*' --no-browser --allow-root"

pyspark \
    --driver-memory 2g \
    --executor-memory 2g \
    --num-executors 1 \
    --executor-cores 1 \
    --conf spark.driver.maxResultSize=8g \
    --conf spark.network.timeout=2000 \
    --queue default \
    --master yarn-client > $HOME/jupyter.log 2>&1 &

pyspark --master spark://localhost:7077 > $HOME/jupyter.log 2>&1 &

num_rdd = sc.parallelize(list(range(10000)))
num_rdd.map(lambda x: x * x).reduce(lambda a, b: a + b)

$HADOOP_HOME/sbin/stop-all.sh \
    && $SPARK_HOME/sbin/stop-all.sh \
    && $SPARK_HOME/sbin/stop-history-server.sh
```

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark History](http://localhost:18080)
