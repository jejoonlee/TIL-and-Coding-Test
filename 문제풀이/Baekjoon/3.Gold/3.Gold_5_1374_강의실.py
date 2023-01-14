import sys
sys.stdin = open('input.txt')

import heapq

N = int(input())

lecture = []
for _ in range(N):
    lecture.append(tuple(map(int, input().split())))

# 강의를 강의 시작하는 시간 기준으로 정렬
lecture.sort(key=lambda x: x[1])

# 강의 끝나는 시간들을 heap으로 정렬한다
# heap은 min-heap이 기본이다!
lecture_finish = []
count = 0

for lect in lecture:
    # 강의가 시작하는 시간과 lecture_finish[0]의 즉 강의가 제일 빠르게 끝나는 시간과 비교를 한다
    # 비교를 해서 강의 시간이랑 lecture_finish[0]가 같거나 강의 시작 시간이 더 클 때, lecture_finish에서 끝나는 시간을 빼준다
    while lecture_finish and lecture_finish[0] <= lect[1]:
        heapq.heappop(lecture_finish)
    
    # 위에 while문이 성사가 안 될 때, 강의 끝나는 시간을 lecture_finish에 넣는다
    heapq.heappush(lecture_finish, lect[2])
    count = max(count, len(lecture_finish))

print(count)

# lecture.sort(key=lambda x: x[1])
# lecture.sort(key=lambda x : x[2])

# classroom = 0

# while lecture:
#     lecture_room = lecture.pop(0)
#     classroom += 1
#     i = 0

#     while i < len(lecture):
#         if lecture_room[2] <= lecture[i][1]:
#             lecture_room = lecture[i]
#             lecture.pop(i)
#         else:
#             i += 1

# print(classroom)