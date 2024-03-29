Language Modeling
=================

Learned deterministic bigram model
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

Enhancing the model
-------------------

- Consider more than one word of context
- Attempt to learn similarities between words

n-gram model
------------

- Consider multiple prior words

Example
-------

Scaling n-gram models
---------------------

- There are many different words that must be tracked
- One estimate is that there are ~1 million words just in English

Bag-of-words
------------

- A bag-of-words approach can be used that ignores word order
