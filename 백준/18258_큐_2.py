import sys
from collections import deque

queue = deque()
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = input().strip().split(' ')
    
    com, num = command[0], 0
    
    if com == 'push': num = int(command[1])

    if com == 'push': queue.append(num)
    elif com == 'pop' :
        if queue: print(queue.popleft())
        else: print(-1)
    elif com == 'size': print(len(queue))
    elif com == 'empty':
        if queue: print(0)
        else: print(1)
    elif com == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif com == 'back':
        if queue: print(queue[-1])
        else: print(-1)