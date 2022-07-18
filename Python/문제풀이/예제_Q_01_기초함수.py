# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

def cube(a):            # def 으로 시작하여 'cube' 이라는 함수 이름을 만들고, 'a'라는 입력값을 넣는다
    return a ** 3       # return 값을 반환하는 것

a = int(input())
print(cube(a))
