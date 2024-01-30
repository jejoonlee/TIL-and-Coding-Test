import sys

num = int(sys.stdin.readline())

numList = [0] * 10

while num > 0:
    numList[num % 10] += 1
    num //= 10

for i in range(9, -1, -1):
    if numList[i] != 0:
        for _ in range(numList[i]): print(i, end='')