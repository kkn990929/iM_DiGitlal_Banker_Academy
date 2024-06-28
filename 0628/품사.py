# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:44:17 2024

@author: campus4D037
"""

import nltk
from nltk.tokenize import word_tokenize

sent1 = "that after the original Stonewall Inn (modern building pictured) closed in 1969, its space was used by a bagel shop, a Chinese "
w_token = word_tokenize(sent1.lower())

print(nltk.pos_tag(w_token)) # 각 문장들에 tag를 붙여서 출력

## NN추출 (명사추출)
my_tag = ["NN" , "NNP" , "NNS"]
my_word = [word for word, tag in nltk.pos_tag(w_token) if tag in my_tag]

# 분류기호 만들어서 W/T 형태로 만들기
custom_my_word= ['/'.join(item) for item in nltk.pos_tag(w_token)]