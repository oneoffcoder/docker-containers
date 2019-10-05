FROM databricksruntime/standard:latest
LABEL One-Off Coder "info@oneoffcoder.com"

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        python3-dev \
    && apt-get clean

RUN /databricks/conda/bin/conda update -n base -c defaults conda
COPY environment.yml /tmp/environment.yml
RUN /databricks/conda/bin/conda env update --file /tmp/environment.yml
RUN /databricks/conda/envs/dcs-minimal/bin/python -m spacy download en_core_web_lg \
    && /databricks/conda/envs/dcs-minimal/bin/python -m nltk.downloader all

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*