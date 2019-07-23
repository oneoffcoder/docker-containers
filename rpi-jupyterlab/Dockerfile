FROM vangjee/rpi-miniconda
LABEL Thanos "vangjee@gmail.com"
ENV CONDA_ENV=/root/miniconda
ENV JUPYTER_TYPE=lab
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install supervisor -y
COPY requirements.txt /tmp/requirements.txt
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY setup.sh /tmp/setup.sh
COPY environment.yml /tmp/environment.yml
RUN /tmp/setup.sh
RUN rm -f /tmp/environment.yml
RUN rm -f /tmp/setup.sh
RUN rm -f /tmp/requirements.txt
RUN mkdir /ipynb
EXPOSE 8888
VOLUME ["/ipynb"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]