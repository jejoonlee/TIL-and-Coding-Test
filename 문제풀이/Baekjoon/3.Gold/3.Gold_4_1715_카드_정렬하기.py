import sys
sys.stdin = open("input.txt")

import heapq

N = int(input())

heap = []

for n in range(N):
    heapq.heappush(heap, int(input()))

answer = 0
while True:

    if len(heap) <= 1:
        break
    else:
        compare = 0
        for _ in range(2):
            cards = heapq.heappop(heap)
            compare += cards

        answer += compare
        heapq.heappush(heap, compare)
        
print(answer)