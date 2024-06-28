# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:00:13 2024

@author: campus4D037
"""
class DOGS:
    def __init__(self , name, age, color):
        self.name = name
        self.age = age
        
        self.color = color # 여기까지 속성
        # self는 무조건!(일단 나 자신으로 취급 + 변수 입력시 변환)
    def bark(self):
        print(f'이름은{self.name} 나이는{self.age} 색상은{self.color}')
        
dog1 = DOGS('asdf', 5, 'blue')
dog1.bark() #여기는 메소드

# 기존에 설계되어 있는 클래스의 속성이나 메소드를 상속받아 사용하는 기능
# dog클래스를 DOG_child로 상속받기
class DOG_child(DOGS):
    def __init__(self):
        DOGS. #위쪽의 부모 class(DOGS)를 받아서 DOGS.bark라는 함수를 가져올 수 있음.
    