import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

array.sort(key=lambda x: -x)
array = deque(array)

ans = 0

while len(array) != 0 :
    if array[1]:
        a = array.popleft()
        b = array.popleft()
        
        if a * b > 0:
            ans += a * b
        elif a * b < 0:
            ans += a + b
        else:
            if a + b > 0:
                ans += a + b
            elif a + b < 0:
                ans += a* b

print(ans)