# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:02:30 2024

@author: campus4D037
"""
# 1-1
import nltk
from nltk.tokenize import sent_tokenize , word_tokenize , WordPunctTokenizer

# 문장 토큰화
sentence = "The cat (Felis catus), commonly referred to as the domestic cat or house cat, is a small domesticated carnivorous mammal."

token_sent = sent_tokenize(sentence) 
# nltk내의 tokenaizer
print(sent_tokenize(sentence))
# 마침표 느낌표 물음표 기준으로 문장구분


#단어 토큰화
print(word_tokenize(sentence))



# 한글 test
kor_sentence = "국제학술지 '사이언스 어드밴시스'"

print(sent_tokenize(kor_sentence))

print(word_tokenize(kor_sentence))


# WordPunctTokenizer
print(WordPunctTokenizer().tokenize(sentence))

# word_tokenize는 '를 포함 It's => It's
# WordPunctTokenizer는 '도 분리 It's => It is
# 불용어 처리
