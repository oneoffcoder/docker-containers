FROM mysql:latest
LABEL One-Off Coder "info@oneoffcoder.com"

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install git wget -y \
    && apt-get clean

COPY import.sh /root

# RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["mysqld", ""]