
import sys
sys.stdin = open('input.txt')

# 1. 배열에 정수 x를 넣는다. 정수는 0을 제외
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거
# 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거

import heapq

T = int(input())
array = []

heapq.heapify(array)

for _ in range(T):
    x = int(input())
    num = (abs(x), x)

    if x == 0:
        if len(array) != 0:
            a = heapq.heappop(array)
            print(a[1])
        else:
            print(0)
    else:
        heapq.heappush(array, num)