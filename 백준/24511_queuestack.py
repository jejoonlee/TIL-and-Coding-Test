import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

info = list(map(int, input().split(" ")))

qs = deque(map(int, input().split(" ")))

m = int(input())

c = list(map(int, input().split(" ")))

answer = []

newQS = deque()

for i in range(n):
    if info[i] == 0:
        newQS.append(qs[i])

for num in c:
    newQS.appendleft(num)
    answer.append(newQS.pop())

print(' '.join(list(map(str, answer))))
