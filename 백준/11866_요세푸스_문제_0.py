
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split(' '))

nList = deque(range(1, n + 1))

answer = []

i = 0
while nList:

    if i == k - 1:
        answer.append(nList.popleft())
        i = 0
    else:
        nList.append(nList.popleft())
        i += 1

print(f"<{', '.join(list(map(str, answer)))}>")