import sys
sys.stdin = open("input.txt")

import heapq

N = int(input())

time = []
for _ in range(N):
    time.append(tuple(map(int, input().split())))

time.sort(key=lambda x: (x[0], x[1]))

heap = []

for start, end in time:

    if len(heap) == 0:
        heapq.heappush(heap, end)
    
    else:
        # 수업이 시작하는 시간이, 수업이 끝나는 시간과 겹치거나 클 때
        # 힙에 있는 숫자를 빼주고, 새로운 끝나는 시간을 넣어준다
        if heap[0] <= start:
            heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        # 수웝이 시작하는 시간이, 수업이 끝나는 시간보다 작으면
        # 힙에 새로운 시간을 추가해준다
        # 이유는 강의가 겹치는 것 때문에
        else:
            heapq.heappush(heap, end)

print(len(heap))