
import sys
sys.stdin = open('input.txt')

# 최소 힙을 구하는 프로그램
# 배열에 자연수 x를 넣는다
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다

import heapq

N = int(sys.stdin.readline())
array = []
heapq.heapify(array)

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(array) == 0:
            print(0)
        else:
            print(heapq.heappop(array))

    else:
        heapq.heappush(array, x)