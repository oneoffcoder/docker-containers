![One-Off Coder Logo](../logo.png "One-Off Coder")

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

[Image](https://hub.docker.com/r/oneoffcoder/conda-nlp)

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
docker run -it \
    -v $HOME/git/docker-containers/conda-nlp/ipynb:/ipynb \
    -p 8888:8888 \
    conda-nlp:local
```

Observe it: [http://localhost:8888](http://localhost:8888).

# Take a Look!

Check out [Robert Schapire](https://en.wikipedia.org/wiki/Robert_Schapire).

# Citation

```
@misc{oneoffcoder_conda_nlp_2019, 
title={Docker container for Natural Language Processing with Jupyter Lab}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/conda-nlp}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jul}}
```
