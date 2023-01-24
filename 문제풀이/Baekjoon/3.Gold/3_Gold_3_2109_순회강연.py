import sys
sys.stdin = open("input.txt")

import heapq

# N = int(input())

# days = [False] * 10001
# lecture = []
# answer = 0

# for _ in range(N):
#     temp_wage, temp_time = map(int, input().split())
#     heapq.heappush(lecture, (-temp_wage, temp_time))

# while lecture:
#     wage, time = heapq.heappop(lecture)

#     if days[time] == False:
#         days[time] = True
#         answer += wage
#     else:
#         time -= 1
#         while time > 0:
#             if days[time] == False:
#                 days[time] = True
#                 answer += wage
#                 break
#             else:
#                 time -= 1

# print(-answer)

# Heap은 강의 날짜보다 더 적어야 한다
# 그리고 마지막으로 Heap들을 더하면 됨

N = int(input())

schedule = []

for _ in range(N):
    money, day = map(int, input().split())
    schedule.append((day, money))

schedule.sort(key=lambda x : x[0])

heap = []

for time, pay in schedule:
    heapq.heappush(heap, pay)

    if len(heap) > time:
        heapq.heappop(heap)

print(sum(heap))