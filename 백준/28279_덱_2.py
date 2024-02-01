
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dq = deque()

for _ in range(t):
    command = input().strip()

    com, num = int(command[0]), 0

    if len(command) > 1: num = command[2:]

    if com == 1: dq.appendleft(num)
    elif com == 2: dq.append(num)
    elif com == 3: 
        if dq: print(dq.popleft())
        else: print(-1)
    elif com == 4:
        if dq: print(dq.pop())
        else: print(-1)
    elif com == 5: print(len(dq))
    elif com == 6:
        if dq: print(0)
        else: print(1)
    elif com == 7:
        if dq: print(dq[0])
        else: print(-1)
    elif com == 8:
        if dq: print(dq[-1])
        else: print(-1)