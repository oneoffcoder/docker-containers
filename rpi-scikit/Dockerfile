FROM vangjee/rpi-jupyterlab
LABEL Thanos "vangjee@gmail.com"
RUN apt-get update -y 
RUN apt-get upgrade -y
COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
RUN rm -f /tmp/environment.yml
