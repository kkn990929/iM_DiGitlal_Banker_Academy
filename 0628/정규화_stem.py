# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:16:25 2024

@author: campus4D037
"""
# Stemming 사전에 없는 단어형태로 바뀔 수 있음
    # ex) 작은 작다 작거나 에서 '작'을 추출
    
    
# 1-5 정규화
from nltk.stem import LancasterStemmer, PorterStemmer
from nltk.tokenize import word_tokenize
# pt_stem = PorterStemmer()
# print(pt_stem.stem('cooking')) # cook으로 출력 
# print(pt_stem.stem('cook'))
# print(pt_stem.stem('cookery')) # cookeri로 출력 y로 끝나면 i로 바뀜


lc_stem = LancasterStemmer() # 특정패턴없음 ex) y->i
# print(lc_stem.stem('cooking')) # cook으로 출력 
# print(lc_stem.stem('cook'))
# print(lc_stem.stem('cookery')) # cookery로 출력



sent1 = "that after the original Stonewall Inn (modern building pictured) closed in 1969, its space was used by a bagel shop, a Chinese "
w_token = word_tokenize(sent1.lower())

result_tok = [lc_stem.stem(word) for word in w_token ]

