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
