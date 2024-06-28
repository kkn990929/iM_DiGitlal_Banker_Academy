# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:11:42 2024

@author: campus4D037
"""
# 1-3
#특수문자 제거
from nltk.tokenize import RegexpTokenizer #Regular Expression 
rg_token = RegexpTokenizer("[\w']{3,}")
# 문자 숫자 특수문자 etc upperstropy까지
# [\w']{3,} => upperstropy가 들어가 있는 단어까지 포함해서 3글자 추출
# [\w']+
print(rg_token.tokenize("It's very_ _good! ~ㅁㄴㅇㄹ"))


#대문자 <-> 소문자 with lower , upper
sent1 = "It's very_ _good!"
print(rg_token.tokenize(sent1.upper()))
print(rg_token.tokenize(sent1.lower()))



