# 약수 중에 소수인 숫자 (소인수)
# 소인수분해는 어떤 숫자의 소인수의 곱으로 나타낸 것이다

inputNum = int(input('1보다 큰 숫자를 입력해주세요 : '))

n = 2

while n <= inputNum:

    if inputNum % n == 0:
        print(f'소인수 : {n}')
        inputNum /= n

    else:
        n += 1