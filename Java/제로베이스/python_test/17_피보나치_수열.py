
# 세 번째 항은 두 번째 항과 첫 번쨰 항을 더한 합이다
# 1 1 2 3 5 8 13 21

inputN = int(input('n 입력 : '))

prevNum = 1
nextNum = 1
sumNum = 0
n = 1

while n <= inputN:

    if n == 1 or n == 2:
        sumNum += nextNum

    else:
        valNum = prevNum + nextNum
        prevNum = nextNum
        nextNum = valNum
        sumNum += valNum

    n += 1 

print(f'{inputN}번째 항의 값 : {nextNum}')
print(f'{inputN}번째 항까지의 합 : {sumNum}')