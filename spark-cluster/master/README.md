# Notes

## Testing

* [HDFS](http://localhost:9870)
* [YARN](http://localhost:8088)
* [Spark](http://localhost:8080)
* [Spark History](http://localhost:18080)

```bash
# test hadoop/spark services
jps

# test listening ports
netstat -tulnp | grep LISTEN

# test hadoop
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 5 10

# test yarn
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 1 50

# test spark with yarn
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100

# test spark standalone
$SPARK_HOME/bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master spark://localhost:7077 \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    100
```