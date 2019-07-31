FROM oneoffcoder/rpi-base
LABEL One-Off Coder "info@oneoffcoder.com"
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
VOLUME ["/darknet/cfg", "/darknet/weight"]