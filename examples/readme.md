Examples
========

This directory includes the examples shown in class.

Data Sources
------------

### lm-wiki.txt

This is the lead section of the Wikipedia page for language models. Refs and other formatting have been adjusted.

### tinystories-100.txt

This is the first 100 items from the tinystories dataset. Stories are concatenated and separated by 4 newlines. Unicode characters are replaced with the closest ascii representations.

```python
import requests
from unidecode import unidecode

stories = requests.get("https://datasets-server.huggingface.co/rows?dataset=roneneldan%2FTinyStories&config=default&split=train&offset=0&length=100").json()

text = '\n\n\n\n'.join([s['row']['text'] for s in stories['rows']])

text = unidecode(text)

with open("tinystories-100.txt", "w") as f:
    f.write(text)
```