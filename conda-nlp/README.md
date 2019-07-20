# Purpose

The purpose of this container is to create a Natural Language Processing (NLP) [Conda](https://anaconda.org/) environment with Jupyter Lab.

Here are some NLP packages installed.

* [spaCy](https://spacy.io/) with all English models
* [gensim](https://radimrehurek.com/gensim/)
* [nltk](https://www.nltk.org/)
* [textblob](https://textblob.readthedocs.io/en/dev/)
* [Pattern](https://www.clips.uantwerpen.be/pages/pattern)
* [polyglot](https://github.com/aboSamoor/polyglot)
* [stanfordcorenlp](https://github.com/Lynten/stanford-corenlp)
* [Vocabulary](https://github.com/tasdikrahman/vocabulary)
* [PyNLPl](https://github.com/proycon/pynlpl)
* [wordcloud](https://github.com/amueller/word_cloud)
* [scattertext](https://github.com/JasonKessler/scattertext)

# Docker Hub

[Image](https://hub.docker.com/r/vangjee/conda-nlp)

# Docker

Build it.

```bash
./build.sh
```

Run it.

```bash
docker run -it -p 8888:8888 conda-nlp:local
```

Run it with a mounted host folder.

```bash
docker run -it -v /home/user/ipynb:/ipynb -p 8888:8888 conda-nlp:local
```

Observe it: [http://localhost:8888](http://localhost:8888).

# Citation

```
@misc{vang_conda_nlp_2019, 
title={Docker container for Natural Language Processing with Jupyter Lab}, 
url={https://github.com/vangj/docker-containers/tree/master/conda-nlp}, 
journal={GitHub},
author={Vang, Jee}, 
year={2019}, 
month={Jul}}
```
