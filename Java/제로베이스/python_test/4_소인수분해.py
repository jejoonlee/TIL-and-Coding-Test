
inputNum = int(input('1보다 큰 숫자를 입력해주세요 : '))

n = 2
x = 1
numList = []

while n <= inputNum:

    if inputNum % n == 0:
        print(f'소인수 : {n}')

        if numList.count(n) == 0:
            numList.append(n)
        elif numList.count(n) == 1:
            numList.remove(n)
        inputNum /= n

    else:
        n += 1

print(numList)