# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:27:28 2024

@author: campus4D037
"""

# 1-4
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer #Regular Expression 

en_stop = set(stopwords.words('english')) #영어 불용어 179개

text1 = "Sorry, I couldn't go to movie yesterday"

# my_stop = ["i" , "go"] 
# 나만의 stopwords를 만들기

# 전처리
re_tok = RegexpTokenizer("[\w']+")
token_sent = re_tok.tokenize(text1.lower())

# 여기까지 불필요한 특수문자 제거

# 불용어 제거
result_tok = [word for word in token_sent if word not in en_stop]
result_tok

# my_stop_result = [word for word in token_sent if word not in my_stop]


# 어간 추출 Stemming 사전에 없는 단어형태로 바뀔 수 있음
    # ex) 작은 작다 작거나 에서 '작'을 추출
# Lemma? 사전에 있는 단어로 바뀔 수 있음
    # ex) 작은 작다 작거나 에서 '작'을 추출해 '작다'로 변환
# 결국 단어의 원형을 찾는 행위(함수)

# -> 정규화 => 단어들을 동일하게 변환 후 작업을 진행함
