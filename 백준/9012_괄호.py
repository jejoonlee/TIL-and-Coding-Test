import sys
from collections import deque

t = int(input())

for _ in range(t):
    symbols = input().strip()
    flag = True
    check = deque()

    for s in symbols:
        if s == '(': check.appendleft(s)
        elif len(check) > 0: 
            check.pop()
        elif len(check) == 0:
            flag = False

    if flag == True and len(check) == 0: print('YES')
    else: print('NO')