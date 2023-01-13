import sys
sys.stdin = open("input.txt")

N = int(input())

meeting = []
for _ in range(N):
    meeting.append(tuple(map(int, input().split())))

# 빨리 시작하는 기준으로 정렬
meeting.sort(key=lambda x: x[0])
# 그 다음 빨리 시작하는 정렬 기준으로, 빨리 끝나는 기준으로 정렬
meeting.sort(key=lambda x: x[1])

cnt = 1
meeting_now = meeting[0]

for i in range(1, N):
    if meeting[i][0] >= meeting_now[1]:
        meeting_now = meeting[i]
        cnt += 1

print(cnt)