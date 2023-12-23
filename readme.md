# QA Generator

This service generate multiple choice questions (MCQ) about generic text. To do this, I implement three modules:

- Keyword Extractor: to extract keywords from a passage
- Question Generator: to generate a question from a keyword and passage
- Distractors generator: to generate keyword distractors

## Structure of the Project

There are three branches in github repository, one for each keyword extractor.

### keyExtractor

There are three alternatives to extract key phrases that have been implemented:

- keyBert[[1]](#1) (based on Bert transformer)
- multipartiteGraph[[2]](#2)
- Rake[[3]](#3) (rapid automatic keyword extractor)

### generateDistractors

This module generate wrong alternatives, given keyword using sense2vec.[[4]](#4)

### questionGeneration

T5 transformer is trained on SQUAD dataset to generate question from keyword and passage.

## Execute the Project

Each module is implemented as docker image. To build each one, execute `build.sh` and to set up services, run `run.sh`. To test if everything runs correctly, execute `test.py`

## References

<a id="1">[1]</a>
Bert: Pre-training of deep bidirectional transformers for language understanding.
Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina(2018).

<a id="2">[2]</a>
Unsupervised keyphrase extraction with multipartite graphs. Boudin, Florian(2018).

<a id="3">[3]</a>
Automatic keyword extraction from individual documents. Rose, Stuart and Engel, Dave and Cramer, Nick and Cowley, Wendy(2010).

<a id="4">[4]</a>
sense2vec-a fast and accurate method for word sense disambiguation in neural word embeddings. sTrask, Andrew and Michalak, Phil and Liu, John(2015).
