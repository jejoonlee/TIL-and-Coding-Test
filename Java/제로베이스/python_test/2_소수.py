

inputNum = int(input("0보다 큰 수 입력: "))

numList = [0] * (inputNum + 1)

for n in range(2, inputNum + 1):
    
    for k in range(n + n, inputNum + 1, n):
        if numList[k] == 0:
            numList[k] = 1

print(numList)

for n in range(2, inputNum + 1):
    if numList[n] == 0:
        print(f'{n} : 소수!!')
    else:
        print(f'{n} : 합성수!!')