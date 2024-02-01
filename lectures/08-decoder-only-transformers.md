Decoder-only Transformers
=========================

GPT
---

- Generative Pre-Trained Transformer
- Decoder-only transformer
- [Paper](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
- SOTA at most NLP tasks when released

---

![Transformer](media/transformer-basic.png)

---

![GPT](media/gpt.png)

Pretraining Data
----------------

> We use the BooksCorpus dataset for training the language model. It contains over 7,000 unique unpublished books from a variety of genres including Adventure, Fantasy, and Romance.

Size
----

> We trained a 12-layer decoder-only transformer with masked self-attention heads (768 dimensional states and 12 attention heads). For the position-wise feed-forward networks, we used 3072 dimensional inner states.
