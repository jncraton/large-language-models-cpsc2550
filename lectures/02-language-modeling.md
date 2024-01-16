Language Modeling
==================

Model
-----

- A model is an informative representation of an object, person, or system.

---

![Molecular Model](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Beta-D-Gulopyranose_Molek%C3%BClbaukasten_9288.JPG/481px-Beta-D-Gulopyranose_Molek%C3%BClbaukasten_9288.JPG)

---

![Supply and Demand Economic Model](https://upload.wikimedia.org/wikipedia/commons/7/7a/Supply-and-demand.svg){height=540px}

Simple Language Models
----------------------

n-grams
-------

- n-gram is a sequence of n adjacent symbols in particular order
- Examples include letters in a word or words in a text
- A unigram (or 1-gram) would be a single word

Hard-coded unigram model
------------------------

- Considers only the previous word when determining the next
- We write the rules to determine the next word
- No machine learning involved

Example
-------

Learned deterministic unigram model
-----------------------------------

- Rules for learning which word comes next can be learned
- Instead of writing the rules as code, we can write the code to learn the rules

Example
-------

Sampling
--------

- Our previous model always produces the same output
- We can instead store more information in our model and choose from weighted distribution of next words

Example
-------
