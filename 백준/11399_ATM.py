import sys
input = sys.stdin.readline

n = int(input())

times = list(map(int, input().split(' ')))

timeSort = []

for i in range(n):
    timeSort.append([i, times[i]])

timeSort.sort(key=lambda x : x[1])

answer, accumulateNum = 0, 0

for i in range(n):
    time = timeSort[i][1]
    accumulateNum += time
    answer += accumulateNum

print(answer)