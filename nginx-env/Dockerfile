FROM nginx:alpine  
LABEL Thanos "jvang@bechtel.com"
COPY ./doit.sh /tmp/doit.sh
COPY ./supervisord.conf /etc/supervisord.conf
RUN apk update && apk add --no-cache supervisor bash
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]