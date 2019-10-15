FROM ubuntu:latest
LABEL One-Off Coder "info@oneoffcoder.com"

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_PREFIX=/usr/local/hadoop
ENV HADOOP_YARN_HOME=${HADOOP_PREFIX}
ENV HADOOP_CONF_DIR=${HADOOP_PREFIX}/etc/hadoop
ENV YARN_LOG_DIR=${HADOOP_YARN_HOME}/logs
ENV YARN_IDENT_STRING=root
ENV HADOOP_MAPRED_IDENT_STRING=root
ENV SPARK_HOME=/usr/local/spark
ENV PATH=${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${HADOOP_PREFIX}/bin:${PATH}

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install openjdk-8-jdk wget \
    && apt-get clean

# setup hadoop
RUN wget -q http://apache.mirrors.tds.net/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz -O /tmp/hadoop-3.2.1.tar.gz \
    && tar -xzf /tmp/hadoop-3.2.1.tar.gz -C /usr/local/ \
    && ln -s /usr/local/hadoop-3.2.1 /usr/local/hadoop \
    && rm -fr /usr/local/hadoop/etc/hadoop/* \
    && mkdir /var/hadoop \
	&& mkdir /var/hadoop/hadoop-datanode \
	&& mkdir /var/hadoop/hadoop-namenode \
	&& mkdir /var/hadoop/mr-history \
	&& mkdir /var/hadoop/mr-history/done \
	&& mkdir /var/hadoop/mr-history/tmp
COPY hadoop/etc/hadoop/* /usr/local/hadoop/etc/hadoop/

# setup spark
RUN wget -q http://mirrors.advancedhosters.com/apache/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz -O /tmp/spark-2.4.4-bin-hadoop2.7.tgz \
    && tar -xzf /tmp/spark-2.4.4-bin-hadoop2.7.tgz -C /usr/local/ \
    && ln -s /usr/local/spark-2.4.4-bin-hadoop2.7 /usr/local/spark \
    && rm -fr /usr/local/spark/conf/*
COPY spark/conf/* /usr/local/spark/conf/

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*