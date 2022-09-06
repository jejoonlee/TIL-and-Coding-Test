import sys
sys.stdin = open('input.txt')

# 1부터 N의 숫자가 있음 (1이 제일 위)
# 1. 맨 위에 있는 숫자를 바닥으로 버리기
# 2. 그 다음의 숫자는 맨 뒤로 넣기
# 이걸 하나 남을때까지 반복한다

from collections import deque

N = int(input())

lst = []

for n in range(1, N + 1):
    lst.append(n)

queue = deque(lst)

while len(queue) != 1:
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(*queue)