FROM oneoffcoder/rpi-base
LABEL One-Off Coder "info@oneoffcoder.com"
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
EXPOSE 8888 8070 8090
VOLUME ["/darknet/cfg", "/darknet/data", "/darknet/weight", "/darknet/video", "/darknet/image", "/darknet/log", "/darknet/backup", "/root/scripts"]