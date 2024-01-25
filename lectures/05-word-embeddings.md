Word Embeddings
===============

Word Meaning
------------

- Algorithms that work with text need to model relationships between words
- Modern computers are built around numbers
- How might we convert the meaning of a word into numbers?

Tokens
------

- Segments of text with semantic meaning
- Represented as a number
- Typically provided as input to a neural network using 1-hot coding

---

![](https://upload.wikimedia.org/wikipedia/commons/9/99/Neural_network_example.svg){height=540px}

Numeric Representation
----------------------

- Create vectors to represent words
- Basis vectors could represent properties of a word

---

Consider basis vectors such as `political power` and `gender`. 

- How would a queen be represented? 
- How would congressman be represented?

---

![Word Vector Math](media/word2vec.png)

Word Embedding
--------------

A word embedding is a a vector that encodes the meaning of a word so that words that are closer in the vector space are expected to have similar meanings

Learning Embeddings
-------------------

- It is tedious to the point of impossibility to manually create embeddings
- What if these could be learned from analyzing texts?

word2vec
--------

- Learns embeddings by analyzing nearby words in a large corpus
- Word similarity is defined as their cosine distance

Example
-------

