Transformers
============

Simple models
-------------

- Bigram models are simple, but unable to capture complexity

n-grams
-------

- N-gram models do not scale well
- Context combinations grow quickly
- Models will tend to repeat text from training data

Bag of Words
------------

- One approach to extend context is to treat prior words as an unordered set rather than a list
- This makes larger contexts possible, but loses important information about word order
- Bag-of-words models may also repeat training data in certain cases

Recurrent Neural Networks
-------------------------

- RNNs are one approach to modeling language
- Model maintains internal state
- Uses internal state and current word to predict next word

---

![RNN](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Recurrent_neural_network_unfold.svg/1280px-Recurrent_neural_network_unfold.svg.png)

RNN Challenges
--------------

- Expensive training
- Long context is difficult in many implementations due to vanishing gradients

Transformers
------------

- Introduced in [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- Provide efficient training
- Uses attention mechanism to avoid under weighting less recently seen data

---

![Transformer [(source)](http://jalammar.github.io/illustrated-transformer/)](media/transformer-basic.png)

---

![Transformer Decoding [(source)](http://jalammar.github.io/illustrated-transformer/)](media/transformer-decoding.mp4)

---

![Transformer Details [(source)](http://jalammar.github.io/illustrated-transformer/)](media/transformer-details.png)

Transformer Weaknesses
----------------------

- Limited context size
- Attention context has an n^2 memory requirement during inference
