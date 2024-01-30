
n = int(input())

answer = 0

for i in range(n, -1, -1):

    addNum, tempNum = i, i

    while tempNum > 0:
        addNum += tempNum % 10
        tempNum //= 10

    if addNum == n:
        answer = i

print(answer)