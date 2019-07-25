FROM oneoffcoder/rpi-nlp
LABEL One-Off Coder "info@oneoffcoder.com"
COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
COPY output-artifacts/ /tmp/output-artifacts
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
RUN rm -f /tmp/environment.yml