Exam Review
===========

LLM Powered Applications
------------------------

- [Phind](https://www.phind.com)
- [Poe](https://poe.com)
- [ChatGPT](https://chat.openai.com/)
- [Perplexity](https://www.perplexity.ai/)

Model
-----

- A model is an informative representation of an object, person, or system.

Language Model
--------------

- Probabilistic model of a natural language

Bigram Language Model
---------------------

- Extremely limited model
- Only considers the previous word while predicting the next

Token
-----

- Small segment of text
- May be an entire word
- May be multiple words
- May be a single character

Machine Learning
----------------

- Building algorithms that can learn from data and generalize to unseen data

Training
--------

- The process of learning model parameters from data

Token Embedding
---------------

- Learned representation of a token in vector space

Document Embedding
------------------

- Representation of a document in vector space
- Learned by a model so that documents with similar meanings can map to similar vectors
- Can be computed by transformer encoders

Vector similarity
-----------------

- Vectors can be used to represent documents
- It can be useful to measure similarity between documents by comparing vectors
- This is often accomplished using cosine similarity and/or dot product

Transformers
------------

- Popular machine learning architecture
- Achieves excellent results in many areas
- Scales to larger models more effectively than prior architectures

---

![Transformer](media/transformer-basic.png)

BERT
----

- Early encoder-only transformer used for general NLP tasks
- Released in 2018
- Created by researchers at Google

GPT
---

- Early decoder-only transformer used for general NLP tasks
- Released in 2018
- Created by researchers at OpenAI

Fine-tuning
-----------

- Allows models to be adapted for specific use cases
- Can be used to guide models to better follow instructions or respond conversationally

Quantization
------------

- Lowers precision of model parameters
- Reduces size of stored model
- Can improve inference performance

Sampling
--------

- Process of converting token probabilities output by an LLM to a single token selected by a model

Huggingface transformers
------------------------

- Library that can be used for LLM inference
- Very popular and typically has support for new models quickly
- May not be the best choice for CPU inference

llama_cpp_python
----------------

- Python package
- Provides efficient CPU inference for decoder-only LLMs

Interential
-----------

- Hosted inference engine create by AU student
- Available for free inference use in this course
- Can be accessed using HTTP and the Python `requests` package
