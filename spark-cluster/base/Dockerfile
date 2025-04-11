FROM ubuntu:latest

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root
ENV YARN_PROXYSERVER_USER=root
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_YARN_HOME=${HADOOP_HOME}
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV HADOOP_LOG_DIR=${HADOOP_YARN_HOME}/logs
ENV HADOOP_IDENT_STRING=root
ENV HADOOP_MAPRED_IDENT_STRING=root
ENV HADOOP_MAPRED_HOME=${HADOOP_HOME}
ENV SPARK_HOME=/usr/local/spark
ENV CONDA_HOME=/usr/local/conda
ENV PYSPARK_MASTER=yarn
ENV PATH=${CONDA_HOME}/bin:${SPARK_HOME}/bin:${HADOOP_HOME}/bin:${PATH}

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install openjdk-17-jdk wget sudo openssh-client openssh-server sshpass supervisor \
    && apt-get -y install nano net-tools lynx \
    && apt-get clean

RUN mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# setup ssh
COPY ubuntu/root/.ssh/* /root/.ssh/

# setup bash
COPY ubuntu/root/.bashrc /root/.bashrc

# setup hadoop
RUN wget -q https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz -O /tmp/hadoop.tar.gz \
    && tar -xzf /tmp/hadoop.tar.gz -C /usr/local/ \
    && ln -s /usr/local/hadoop-3.4.1 /usr/local/hadoop \
    && rm -fr /usr/local/hadoop/etc/hadoop/* \
    && mkdir /usr/local/hadoop/extras \
    && mkdir /var/hadoop \
	&& mkdir /var/hadoop/hadoop-datanode \
	&& mkdir /var/hadoop/hadoop-namenode \
	&& mkdir /var/hadoop/mr-history \
	&& mkdir /var/hadoop/mr-history/done \
	&& mkdir /var/hadoop/mr-history/tmp

COPY ubuntu/usr/local/hadoop/extras/* /usr/local/hadoop/extras/

# setup spark
RUN wget -q https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz -O /tmp/spark.tgz \
    && tar -xzf /tmp/spark.tgz -C /usr/local/ \
    && ln -s /usr/local/spark-3.5.5-bin-hadoop3 /usr/local/spark \
    && rm /usr/local/spark/conf/*.template

# setup conda
COPY ubuntu/root/environment.yml /tmp/environment.yml
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda env update -n base --file /tmp/environment.yml \
    && $CONDA_HOME/bin/conda update -n root conda -y \
    && $CONDA_HOME/bin/conda update --all -y \
    && $CONDA_HOME/bin/pip install --upgrade pip

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /tmp/spark-events

# setup supervisor
COPY ubuntu/etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf
COPY ubuntu/etc/supervisor/conf.d/ssh.conf /etc/supervisor/conf.d/ssh.conf

EXPOSE 22
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]