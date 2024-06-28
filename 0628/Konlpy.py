# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:18:36 2024

@author: campus4D037
"""
#%%
import nltk
from nltk.tokenize import word_tokenize 
import konlpy
from konlpy.tag import Okt # 트위터 형태소 분석기
#%%

# text1 = """
# 한국인 88%가 유튜브를 사용하는 것으로 나타났다. 유튜브 총 사용시간은 2021년 이후 꾸준히 늘어나고 있다.
# 특히 10대 이하 남자는 한 달에 56시간 유튜브를 시청하는 것으로 집계됐다. 또,
#  유튜브 앱 사용자수 증가에 힘입어 유튜브 뮤직도 국내 음원 서비스 앱 분야 1위를 차지했다.

# 28일 아이지에이웍스 모바일인덱스에 따르면, 
# 지난 5월 기준 유튜브 사용자 수는 4579만명으로 한국 인구수(5175만 명)의 88%를 차지한 것으로 나타났다.
# """
# #%%

# w_token =  word_tokenize(text1)
# print(word_tokenize(text1))
# t = Okt()

# print("형태소 ; ", t.morphs(text1))

#%%

# nltk
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize , RegexpTokenizer
from nltk.stem import PorterStemmer

p_stem = PorterStemmer()

file_name = gutenberg.fileids()
# print(file_name)

doc_blake = gutenberg.open('blake-poems.txt').read()
print("#Number of Characters used : ", len(doc_blake))

token_blake = word_tokenize(doc_blake)
stem_token_blk = [p_stem.stem(token) for token in token_blake]
rege_Token = RegexpTokenizer("[\w']{3,}") # 3글자 이상 단어 추출
reg_token_blk = rege_Token.tokenize(doc_blake) 

from nltk.corpus import stopwords
en_stop = set(stopwords.words('english'))

result_blk = [word for word in reg_token_blk if word not in en_stop]

#전처리 하고 불용어처리한 결과


blk_word_count = dict()
for word in result_blk :
    blk_word_count[word] = blk_word_count.get(word, 0) + 1
# 키(단어)를 기준으로 vlaue(count)에 +1해서 count함
print(len(blk_word_count))

# 카운트 센걸로 정렬하기
sorted_blk = sorted(blk_word_count, key = blk_word_count.get, reverse= True)
# blk_word_count값의 키를 가져와서 내림차순 정렬


# 시각화
for key in sorted_blk[:30] : 
    print(f'{repr(key)} : {blk_word_count[key]} ', end =',')
#dict안에 자료 갯수 카운트 하기 (상위 30개)

import matplotlib.pyplot as plt
w = [blk_word_count[key] for key in sorted_blk]
plt.plot(w)
plt.show()

# 상위 n개의 data 보여주기 코드
n = sorted_blk[:20][::-1] # 전체리스트 역순
w = [blk_word_count[key] for key in n]
#barh => 가로막대
plt.barh(range(len(n)), w, tick_label = n)
plt.show()


# wordcloud
from wordcloud import WordCloud
WC = WordCloud().generate(doc_blake)
plt.axis("off")
plt.imshow(WC , interpolation = 'bilinear')
plt.show()
