FROM continuumio/miniconda3
LABEL Thanos "vangjee@gmail.com"
RUN apt-get update
RUN apt-get install supervisor -y
COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN /tmp/setup.sh
RUN mkdir /ipynb
EXPOSE 8888
VOLUME ["/ipynb"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]