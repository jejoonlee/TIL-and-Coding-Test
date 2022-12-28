import sys
import heapq

sys.stdin = open('input.txt')

N = int(input())

time = []
for n in range(N):
    s, e = map(int, input().split())
    time.append((s, e))

time.sort(key=lambda x:x[0])
room = []

heapq.heappush(room, time[0][1])

for i in range(1,N):
    if room[0] <= time[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappush(room, time[i][1])

print(len(room))