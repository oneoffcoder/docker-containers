#!/bin/bash

service ssh start
echo "started ssh"

python /usr/local/bin/configure-spark.py
cp /usr/local/spark/conf/spark-env.temp /usr/local/spark/conf/spark-env.sh
rm -f /usr/local/spark/conf/spark-env.temp
echo "configured spark"

$HADOOP_HOME/sbin/start-all.sh
echo "started hadoop"

$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver
echo "started job history server"

$SPARK_HOME/sbin/start-all.sh
echo "started spark"

$SPARK_HOME/sbin/start-history-server.sh
echo "started spark history"

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