# # 계산기
# a,b값 받아서 사칙연산 계산
# while

# 함수
num1 = float(input('숫자 1 입력 '))
num2 = float(input('숫자 2 입력 '))
mark = input('연산자 입력 ')

while text == '종료':
    def cal_func(num1,num2,mark):
        
        if mark == '+':
            print(num1, '+' ,num2, '=', num1+num2)
        elif mark == '-':
            print(num1, '-' ,num2, '=', num1-num2)
        elif mark == '/':
            if num1 == 0 or num2 == 0:
                print('0으로 나눌 수 없음')
            else:
                print(num1 ,'/' ,num2, '=' ,num1/num2)
        elif mark == '*':
            print(num1 ,'*', num2, '=' ,num1*num2)
            
        
cal_func(num1, num2, mark)



