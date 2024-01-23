
inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n 입력 : '))

n = 1
valNum = inputN1

while n <= inputN:

    print(f'{n}번째 항의 값: {valNum}')
    valNum *= inputR
    n += 1


# 몇 번째 항의 숫자
# an = a1 * r ^ (n - 1)
print(f'{inputN}번째 항의 값: {inputN1 * (inputR ** (inputN - 1))}')


# 등비 수열의 합
# a1 * (1 - (r ^ n)) / (1 - r)