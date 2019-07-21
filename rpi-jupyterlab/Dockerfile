FROM vangjee/rpi-python37
LABEL Thanos "vangjee@gmail.com"
ENV DEBIAN_FRONTEND=noninteractive
ENV JUPYTER_TYPE=lab
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install wget supervisor default-libmysqlclient-dev python-dev build-essential -y
RUN pip3.7 install jupyter jupyterlab
RUN apt-get --purge remove wget build-essential default-libmysqlclient-dev python-dev build-essential -y
RUN apt-get autoremove -y
RUN apt-get clean
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN mkdir /ipynb
EXPOSE 8888
VOLUME ["/ipynb"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]