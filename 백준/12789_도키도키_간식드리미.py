import sys
from collections import deque

stack = deque()

n = int(input())
queue = deque(map(int, input().split(" ")))

number = 1

while queue:

    num = queue.popleft()
    stack.append(num)
    
    while stack:
        if stack[-1] == number:
            stack.pop()
            number += 1
        else:
            break
    
if not stack and not queue: print('Nice')
else: print('Sad')