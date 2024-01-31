
import sys

nDict = {}

n = int(sys.stdin.readline())

for num in list(map(int, sys.stdin.readline().split(' '))):
    if num in nDict: nDict[num] += 1
    else: nDict[num] = 1

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split(' ')))

result = [0] * m

for i in range(len(mList)):
    if mList[i] in nDict:
        result[i] = nDict[mList[i]]

print(' '.join(list(map(str, result))))