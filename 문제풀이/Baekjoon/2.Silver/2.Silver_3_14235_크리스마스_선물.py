
import sys
sys.stdin = open("input.txt")

import heapq

N = int(input())

stops = []

for _ in range(N):
    stops.append(tuple(map(int, input().split())))

heap = []

for i in range(N):
    
    if stops[i][0] != 0:
        
        for j in range(1, stops[i][0] + 1):
            heapq.heappush(heap, -stops[i][j])

    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)