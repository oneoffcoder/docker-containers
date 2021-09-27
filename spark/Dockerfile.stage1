FROM spark0:local

ENV SPARK_WORKER_INSTANCES="1"
ENV SPARK_WORKER_CORES="1"
ENV SPARK_WORKER_MEMORY="1g"

# setup hadoop
COPY ubuntu/usr/local/hadoop/etc/hadoop/* /usr/local/hadoop/etc/hadoop/
COPY ubuntu/usr/local/hadoop/extras/* /usr/local/hadoop/extras/

# setup spark
COPY ubuntu/usr/local/spark/conf/* /usr/local/spark/conf/

# setup supervisor
COPY ubuntu/etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf
COPY ubuntu/etc/supervisor/conf.d/all.conf /etc/supervisor/conf.d/all.conf
COPY ubuntu/usr/local/bin/* /usr/local/bin/

EXPOSE 9870 8020 8042 8088 9864 19888 8080 18080 4040 7077

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]