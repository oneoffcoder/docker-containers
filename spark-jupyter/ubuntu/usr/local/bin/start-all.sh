#!/bin/bash

service ssh start
echo "started ssh"

$HADOOP_HOME/sbin/start-all.sh
echo "started hadoop"

$SPARK_HOME/sbin/start-all.sh
echo "started spark"

$SPARK_HOME/sbin/start-history-server.sh
echo "started spark history"

# pyspark --master spark://localhost:7077 > /tmp/jupyter.log 2>&1 &
# options: https://gerardnico.com/db/spark/pyspark/pyspark
$SPARK_HOME/bin/pyspark \
    --packages graphframes:graphframes:0.8.1-spark2.4-s_2.11 \
    --repositories https://repos.spark-packages.org \
    --master $PYSPARK_MASTER > /tmp/jupyter.log 2>&1 &
echo "started pyspark"

if [ -d "/root/ipynb/data" ]; then
    for entry in /root/ipynb/data/*
    do
        hdfs dfs -copyFromLocal -f $entry /$(basename $entry)
        echo "copied $entry to hdfs"
    done
else
    echo "/root/ipynb/data does not exists"
fi

echo "done!"

exit 0