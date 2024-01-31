
import sys

input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().split(' ')))

m = int(input())
mList = list(map(int, input().split(' ')))

result = [0] * m
nDict = {}

for num in nList:
    if num in nDict:
        nDict[num] += 1
    else:
        nDict[num] = 1

for i in range(m):
    if mList[i] in nDict:
        result[i] = nDict[mList[i]]

print(' '.join(list(map(str, result))))