Encoder-only Transformers
=========================

BERT
----

- Bidirectional Encoder Representations from
Transformers
- Encoder-only transformer
- [Paper](https://arxiv.org/pdf/1810.04805.pdf)
- SOTA at most NLP tasks when released

---

![Transformer](media/transformer-basic.png)

---

![BERT](media/bert.png)

Training
--------

> Training of BERT BASE was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total). Training of BERT LARGE was performed on 16 Cloud TPUs (64 TPU chips total). Each pre-training took 4 days to complete.

Size
----

> We primarily report results on two model sizes: BERTBASE (L=12, H=768, A=12, Total Parameters=110M) and BERTLARGE (L=24, H=1024, A=16, Total Parameters=340M).

Pooling
-------

- Each forward pass through the encoder stack results in one embedding
- This means we have an embedding for each token
- These embeddings must be combined in some way to create uniform sized document embeddings

Mean Pooling
------------

- Simple and commonly used pooling approach
- Takes the average of the last hidden state from all encoder outputs