import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

nList = list(map(int, input().split(" ")))

dq = deque()

for i in range(n):
    dq.append([nList[i], i])

answer = []

while dq:
    element = dq.popleft()
    num, idx = element[0], element[1]
    answer.append(idx + 1)

    if len(dq) == 0: break

    if num > 0 : num -= 1

    while num != 0:
        if dq and num < 0:
            dq.appendleft(dq.pop())
            num += 1

        elif dq and num > 0:
            dq.append(dq.popleft())
            num -= 1

print(' '.join(list(map(str, answer))))
