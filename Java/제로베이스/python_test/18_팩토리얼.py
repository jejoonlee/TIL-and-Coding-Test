
inputN = int(input('n 입력 : '))

# ans = 1

# for i in range(1, inputN + 1):
#     ans *= i

# print(f'{inputN}까지의 팩토리얼 결과 : {ans}')


def factorial(n):

    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'{inputN}까지의 팩토리얼 결과 : {factorial(inputN)}')

import math

print(f'{inputN}까지의 팩토리얼 결과 with math.factorial 매서드 : {math.factorial(inputN)}')