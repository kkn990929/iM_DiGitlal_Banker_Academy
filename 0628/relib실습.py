# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:34:26 2024

@author: campus4D037
"""
# 1-2
import re
print(re.findall("[abc]", "How are you, boy")) # ['a', 'b']
# -iter -> 반복하는 메소드
# 현재 string에서 pattern에 있는 요소로 시작하는 단어가 있으면 pattern의 값을 추출?


# 추출
print(re.findall("[0123456798]", "1b5ad5q4564sbasdb4")) # ['1', '5', '5', '4', '5', '6', '4', '4']
# 0~9까지의 숫자를 반환

print(re.findall("[a-z]", "1b5ad5q4564sbasdb4")) # ['b', 'a', 'd', 'q', 's', 'b', 'a', 's', 'd', 'b']
# a~z까지의 문자를 반환

print(re.findall("[0-9 a-z]", "1b5Ad5Q4564sbAsDb4")) # ['1', 'b', '5', 'd', '5', '4', '5', '6', '4', 's', 'b', 's', 'b', '4']
# 0-9 , a-z까지의 숫자,문자를 반환

print(re.findall("[A-Z]", "1b5Ad5Q4564sbAsDb4")) # ['A', 'Q', 'A', 'D']
# A-Z 까지의 문자를 제외하고 반환
print(re.findall("[_]+", "a_b , c__d, e___f")) # ['_', '__', '___']
# 언더바 하나와 그 뒤에 언더바 하나 더 까지 추출. 언더바가 없다면 종료 
print(re.findall("[_]^", "a_b , c__d, e___f")) # []
# '^'사용하면 언더바 빼고 반환

print(re.findall('[o]{2,4}', "oh , hooow aroooe yooooou boooooooooy")) # ['ooo', 'ooo', 'oooo', 'oooo', 'oooo']
# 'o'가 최소 2개부터 4개까지 반복되는 것들 검색 후 반복 if 4개를 넘어가면 반복해서 추출

