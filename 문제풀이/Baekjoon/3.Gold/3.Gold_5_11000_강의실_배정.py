import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())

time = []
for n in range(N):
    s, e = map(int, input().split())
    time.append((s, e))

time.sort(key=lambda x:x[0])
time = deque(time)
room = []

room.append(time.popleft()[1])

