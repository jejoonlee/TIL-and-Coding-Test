import sys
sys.stdin = open("input.txt")

# 하루에 한 과제를 끝낼 수 있고
# 과제마다 마감일이 주어지고
# 과제마다 끝냈을 때 얻을 수 있는 점수가 있다

import heapq

N = int(input())

homework = []

for _ in range(N):
    homework.append(tuple(map(int, input().split())))


day = [False] * 1001
homework.sort(key = lambda x : -x[1])
answer = 0

print(homework)
for time, work in homework:
    i = time

    while i > 0:
        if day[i] == False:
            day[i] = True
            answer += work
            break
        else:
            i -= 1

print(answer)


# max_heap = []
# score = 0


# while homework:
#     time, point = homework.pop(0)
#     heapq.heappush(max_heap, -point)

#     while homework and time == homework[0][0]:
#         same_time, point = homework.pop(0)
#         heapq.heappush(max_heap, -point)
 
#         if len(homework) == 0 or same_time != homework[0][0]:
#             while max_heap and same_time != 0:
#                 final_point = heapq.heappop(max_heap)
#                 score += final_point
#                 same_time -= 1
#             max_heap = []
#             break

# if max_heap:
#     score += sum(max_heap)

# print(-score)