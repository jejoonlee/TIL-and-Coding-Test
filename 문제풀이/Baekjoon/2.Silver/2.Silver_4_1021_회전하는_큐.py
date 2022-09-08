import sys
sys.stdin = open('input.txt')

from collections import deque

N, M = map(int, input().split())
array = list(map(int, input().split()))

queue = []
for n in range(1, N + 1):
    queue.append(n)

array = deque(array)
queue = deque(queue)

# array에 있는 숫자를 queue의 있는 숫자들 중 인덱스를 통해 뒤가 더 가까운지, 앞이 더 가까운지 비교가 가능
# 인덱스와 len(queue) - 인덱스 를 비교해서 0과 가까우면 왼쪽에서, len(queue)와 가까우면 오른쪽에서

cnt = 0

while len(array) != 0:
    if array[0] == queue[0]:
        queue.popleft()
        array.popleft()

    else:
        while array[0] != queue[0]:
            # b의 인덱스, 첫번째 숫자와의 거리
            b = queue.index(array[0])
            # queue의 개수와의 차이, 마지막 숫자와의 거리
            back = len(queue) - b

            if b <= back:
                # 2번 연산
                queue.append(queue.popleft())
                cnt += 1

            else:
                # 3번 연산
                queue.appendleft(queue.pop())
                cnt += 1

print(cnt)