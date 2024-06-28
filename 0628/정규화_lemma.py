# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:33:50 2024

@author: campus4D037
"""

# Lemma? 사전에 있는 단어로 바뀔 수 있음
    # ex) 작은 작다 작거나 에서 '작'을 추출해 '작다'로 변환

from nltk.stem import WordNetLemmatizer

WN_lemma = WordNetLemmatizer()
print(WN_lemma.lemmatize('cooking')) # cooking
print(WN_lemma.lemmatize('cook')) # cook
print(WN_lemma.lemmatize('cookery')) # cookery

# 동사원형으로 변경
print(WN_lemma.lemmatize('cooking', pos = 'v')) # cook

