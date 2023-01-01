import sys

sys.stdin = open("input.txt")
from collections import deque

N = int(input())
pos_array = []
nav_array = []

for _ in range(N):
    num = int(input())
    if num > 0:
        pos_array.append(num)
    else:
        nav_array.append(num)

pos_array.sort(key=lambda x: -x)
nav_array.sort()
pos_array = deque(pos_array)
nav_array = deque(nav_array)

pos_ans = 0
nav_ans = 0

while len(pos_array) != 0:
    if len(pos_array) != 1:
        a = pos_array.popleft()
        b = pos_array.popleft()
        if a != 1 and b != 1:
            pos_ans += a * b
        elif a == 1 or b == 1:
            pos_ans += a + b
    else:
        a = pos_array.popleft()
        pos_ans += a

while len(nav_array) != 0:
    if len(nav_array) != 1:
        a = nav_array.popleft()
        b = nav_array.popleft()
        nav_ans += a * b
    else:
        nav_ans += nav_array.popleft()

print(pos_ans + nav_ans)
