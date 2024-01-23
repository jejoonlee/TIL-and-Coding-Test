
# 100부터 1000사이의 난수에서 공약수와 최대 공약수를 출력하고 서로소인지 출력

import random

numOne = random.randint(100, 1000)
numTwo = random.randint(100, 1000)

while True:

    tempNum = numOne % numTwo

    if tempNum == 0:
        break

    numOne = numTwo
    numTwo = tempNum

print(f'최대공약수 : {numTwo}')

if numTwo == 1:
    print(f'서로소입니다')
else:
    print(f'서로소가 아닙니다')