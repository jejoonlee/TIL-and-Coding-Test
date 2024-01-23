
# 100부터 1000사이의 난수에서 최대공약수와 최소공배수를 구하여라

import random

numOne = random.randint(100, 1000)
numTwo = random.randint(100, 1000)

valOne = numOne
valTwo = numTwo

print(numOne, numTwo)

while True:

    tempNum = numOne % numTwo

    if tempNum == 0:
        break

    numOne = numTwo
    numTwo = tempNum

print(f'최대공약수 : {numTwo}')
print(f'최소공배수: {int((valOne * valTwo) / numTwo)}')