
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split(' ')))

answer = [0] * n

tempNums = []

for i in range(n):
    tempNums.append([nums[i], i])

tempNums.sort(key=lambda x : x[0])
orderNum = 0

for i in range(1, n):
    
    if tempNums[i][0] != tempNums[i - 1][0]:
        orderNum += 1
        answer[tempNums[i][1]] = orderNum
    else:
        answer[tempNums[i][1]] = orderNum

print(' '.join(list(map(str, answer))))