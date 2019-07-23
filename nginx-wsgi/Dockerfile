FROM python:3.7-alpine
LABEL One-Off Coder "info@oneoffcoder.com"
COPY ./conf/supervisord.conf /etc/supervisord.conf
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./flask /app
RUN pip install -vvv --no-cache-dir -r /app/requirements.txt
RUN apk add --no-cache bash nginx supervisor
EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]