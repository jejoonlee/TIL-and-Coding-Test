import sys
sys.stdin = open("input.txt")

import heapq

N = int(input())

days = [False] * 10001
lecture = []
answer = 0

for _ in range(N):
    temp_wage, temp_time = map(int, input().split())
    heapq.heappush(lecture, (-temp_wage, temp_time))

while lecture:
    wage, time = heapq.heappop(lecture)

    if days[time] == False:
        days[time] = True
        answer += wage
    else:
        time -= 1
        while time > 0:
            if days[time] == False:
                days[time] = True
                answer += wage
                break
            else:
                time -= 1

print(-answer)