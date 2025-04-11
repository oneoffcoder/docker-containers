FROM spark-base:latest

COPY ubuntu/etc/supervisor/conf.d/spark.conf /etc/supervisor/conf.d/spark.conf
COPY ubuntu/usr/local/bin/start-all.sh /usr/local/bin/start-all.sh

RUN $HADOOP_HOME/bin/hdfs namenode -format oneoffcoder