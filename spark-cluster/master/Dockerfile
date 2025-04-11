FROM spark-base:latest

COPY ubuntu/etc/supervisor/conf.d/spark.conf /etc/supervisor/conf.d/spark.conf
COPY ubuntu/usr/local/bin/start-all.sh /usr/local/bin/start-all.sh
COPY ubuntu/usr/local/hadoop/etc/hadoop/* /usr/local/hadoop/etc/hadoop/
COPY ubuntu/usr/local/spark/conf/* /usr/local/spark/conf/

RUN $HADOOP_HOME/bin/hdfs namenode -format oneoffcoder