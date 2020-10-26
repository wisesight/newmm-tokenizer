# __newmm-tokenizer__

Standalone Dictionary-based, Maximum Matching + Thai Character Cluster (newmm) tokenizer extracted from [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp).

## __Objectives__
This repository is created for reducing an overall size of original [PyThaiNLP Tokenizer Module](https://www.thainlp.org/pythainlp/docs/2.2/api/tokenize.html). The main objective is to be able to segment Thai sentences into a list of words.

## __Supports__
The module supports Python 3.6+ as follow the original PyThaiNLP repository.

## __Installation__
```
pip install newmm-tokenizer
```

## __How to Use__
```python
from newmm_tokenizer.usecases.tokenizer import word_tokenize

text = 'เป็นเรื่องแรกที่ร้องไห้ตั้งแต่ ep 1 แล้วก็เป็นเรื่องแรกที่เลือกไม่ได้ว่าจะเชียร์พระเอกหรือพระรองดี'
words = word_tokenize(text)

print(words) 
# ['เป็นเรื่อง', 'แรก', 'ที่', 'ร้องไห้', 'ตั้งแต่', ' ', 'ep', ' ', '1', ' ', 'แล้วก็', 'เป็นเรื่อง', 'แรก', 'ที่', 'เลือกไม่ได้', 'ว่า', 'จะ', 'เชียร์', 'พระเอก', 'หรือ', 'พระรอง', 'ดี']
```

## __LICENSE__
Please see the original license of PyThaiNLP [here](https://github.com/PyThaiNLP/pythainlp#licenses)
