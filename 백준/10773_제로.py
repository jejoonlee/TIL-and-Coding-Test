from collections import deque
import sys

input = sys.stdin.readline

addNum = 0

t = int(input())
array = deque()

for _ in range(t):
    n = int(input())

    if n == 0: addNum -= array.popleft()
    else: 
        array.appendleft(n)
        addNum += n

print(addNum)