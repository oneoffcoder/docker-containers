FROM oneoffcoder/rpi-nlp
LABEL One-Off Coder "info@oneoffcoder.com"
RUN apt-get install git -y
COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
COPY tensorflow/ /root/tensorflow/
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
RUN rm -f /tmp/environment.yml