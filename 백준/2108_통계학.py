
import sys

input = sys.stdin.readline

t = int(input())

numList, numAdd, numDict = [], 0, {}

for _ in range(t):
    num = int(input())
    numList.append(num)
    numAdd += num

    if num in numDict: numDict[num] += 1
    else: numDict[num] = 1

numList.sort()
mostNum = max(numDict.values())

print(round(numAdd / t))
print(numList[(t // 2)])

ans = []
for key, value in numDict.items():
    if value == mostNum:
        ans.append(key)

ans.sort()

if len(ans) == 1: print(ans[0])
else : print(ans[1])

print(numList[-1] - numList[0])