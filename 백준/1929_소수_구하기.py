import sys
import math

primeNums = [0] * 1000000
primeNums[0], primeNums[1] = 1, 1

for i in range(2, int(math.sqrt(1000000)) + 1):
    for j in range(i + i, 1000000, i):
        if primeNums[j] == 0:
            primeNums[j] = 1

input = sys.stdin.readline
n, m = map(int, input().split(' '))

for i in range(n, m + 1):
    if primeNums[i] == 0:
        print(i)