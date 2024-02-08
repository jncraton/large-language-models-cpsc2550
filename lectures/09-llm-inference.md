Course Updates
==============

Exam next Thursday
------------------

- Closed book and taken in class on Canvas
- Will primarily focus on terminology, not deeper concepts
- You may use a 1-page hand-written note sheet on the exam

Review
------

- Tuesday will be focused on review of major concepts and terminology

Projects
--------

- We will begin work on projects the following week
- It would be helpful to begin thinking about what you might like to work on and who you may want to work with

Inference Tools
===============

transformers Package
--------------------

- Support all sorts of models
- Tends to be the best supported for new models
- Does not easily support quantization on CPU

---

```python
from transformers import pipeline

generator = pipeline('text-generation',
                     model='openai-community/openai-gpt')

output = generator("Question: What is the capital of France?\n"
                   "Answer:", max_length=50)
print(output[0]['generated_text'])
```

Quantization
------------

- In order to train properly, models typically use fp32, bf32, or bf16 during training
- This level of precision may not provide much benefit during inference
- Because inference is freqently memory bound and narrower fields may allow faster operations there is a performance benefit from shrinking the width of model parameters

---

![Analog to digital quantization](https://upload.wikimedia.org/wikipedia/commons/b/b7/3-bit_resolution_analog_comparison.png){height=540px}

---

![JPEG DCT Output](media/jpeg-dct.svg){height=540px}

---

![JPEG Quantization Matrix](media/jpeg-quantization-matrix.svg){height=540px}

---

![JPEG DCT Output](media/jpeg-quantized-dct.svg){height=540px}

llama_cpp_python
----------------

- Wrapper for llama.cpp
- Provides efficient quantized inference from Python
- Primarly supports decoder-only models

---

```python
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(repo_id="TheBloke/phi-2-GGUF", 
                             filename="phi-2.Q4_K_M.gguf")

llm = Llama(model_path=model_path)

output = llm("User: Please name the planets in the solar system.\n"
             "Assistant:")

print(output["choices"][0]["text"])
```

CTranslate2
-----------

- Provides efficient inference on CPU and GPU
- Supports int8 quantization
- Supports encoder-decoder, encoder-only, and decoder-only models
- [example](../examples/ctranslate2.ipynb)

