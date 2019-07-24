# Purpose

This is a Natural Language Processing (NLP) Conda environment with Jupyter Lab. 

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

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/conda-nlp)

# Docker

Pull it.

```bash
docker pull oneoffcoder/conda-nlp:latest
```

Run it.

```bash
docker run -it -p 8888:8888 oneoffcoder/conda-nlp
```

Run it with a mounted host folder.

```bash
docker run -it -v /home/user/ipynb:/ipynb -p 8888:8888 oneoffcoder/conda-nlp
```

Use it.

*  [http://localhost:8888](http://localhost:8888)
