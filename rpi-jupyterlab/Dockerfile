FROM oneoffcoder/rpi-miniconda
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV JUPYTER_TYPE=lab
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install supervisor -y
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