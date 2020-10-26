from newmm_tokenizer.tokenizer import word_tokenize as newmm_tokenize
from datetime import datetime

text = 'เป็นเรื่องแรกที่ร้องไห้ตั้งแต่ ep 1 แล้วก็เป็นเรื่องแรกที่เลือกไม่ได้ว่าจะเชียร์พระเอกหรือพระรองดี'

start_time = datetime.now()
print(newmm_tokenize(text))
print(f'newmm time: {datetime.now() - start_time}')