FROM continuumio/miniconda3
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

RUN apt-get update
RUN apt-get install supervisor default-libmysqlclient-dev python-dev build-essential -y
COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN /tmp/setup.sh
RUN mkdir /ipynb
EXPOSE 8888
VOLUME ["/ipynb"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]