FROM python:3.7-alpine
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

COPY ./conf/supervisord.conf /etc/supervisord.conf
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./flask /app
RUN pip install -vvv --no-cache-dir -r /app/requirements.txt
RUN apk add --no-cache bash nginx supervisor
EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]