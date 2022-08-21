from collections import deque

# input() 값
N = int(input())

ori = []

for n in range(1, N + 1):
    ori.append(n)

queue = deque(ori)


# 바닦으로 버린 카드
new = []

while len(queue) > 1:
    new.append(queue[0])
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(*new, *queue)