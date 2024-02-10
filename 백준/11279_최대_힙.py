import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    num = int(input())

    if num == 0 and heap:
        print(-heapq.heappop(heap))
    elif num == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, -num)