#!/bin/bash

NAME=$(head -1 /tmp/environment.yml | cut -d' ' -f2)
ENV_PATH=/opt/conda/envs/$NAME

conda update -n base -c defaults conda --yes
conda env create -f /tmp/environment.yml

echo "source activate $NAME" >> ~/.bashrc
echo "PATH=$ENV_PATH/bin:$PATH" >> ~/.bashrc

# $ENV_PATH/bin/python -m spacy download en_core_web_sm
# $ENV_PATH/bin/python -m spacy download en_core_web_md
# $ENV_PATH/bin/python -m spacy download en_core_web_lg
# $ENV_PATH/bin/python -m spacy download en_vectors_web_lg
# $ENV_PATH/bin/python -m nltk.downloader all
# $ENV_PATH/bin/python -m ipykernel install --user --name $NAME --display-name $NAME
# $ENV_PATH/bin/jupyter contrib nbextension install --user
$ENV_PATH/bin/pip install https://download.pytorch.org/whl/cu100/torch-1.1.0-cp37-cp37m-linux_x86_64.whl
$ENV_PATH/bin/pip install https://download.pytorch.org/whl/cu100/torchvision-0.3.0-cp37-cp37m-linux_x86_64.whl

exit 0