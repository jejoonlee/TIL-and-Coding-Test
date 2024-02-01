from collections import deque
import sys

deq = deque()
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = input().strip()
    com, num = command[0], 0

    if len(command) > 1:
        num = int(command[2:])

    if com == '1': deq.appendleft(num)
    elif com == '2':
        if len(deq) > 0: print(deq.popleft())
        else: print(-1)
    elif com == '3': print(len(deq))
    elif com == '4': 
        if len(deq) == 0: print(1)
        else: print(0)
    elif com == '5':
        if len(deq) == 0: print(-1)
        else: print(deq[0])