import sys
sys.stdin = open('input.txt')

# N = int(input())

# meetings = []
# for _ in range(N):
#   a, b = map(int, input().split())
#   meetings.append((a,b))

# meetings.sort()

# result = []
# for i in range(N - 1):
#   cnt = 0
#   j = i + 1
#   while j != N - 1:
#     if meetings[i][1] <= meetings[j][0]:
#       cnt += 1
#       i = j
#       j = i
#     else:
#       j += 1
  
#   result.append(cnt)

# print(result)

# 위에서는 회의 시작하는 시간 기준으로만 정렬을 했다
# 회의를 시작하는 시간 기준으로 정렬을 한 후, 끝나는 시간의 기준으로도 다시 정렬을 해야 한다

# 즉 회의가 빨리 끝나는 순서대로 정렬을 해야 한다. 회의가 빨리 시작하는 순서대로 정렬을 하면 안 된다
N = int(input())
time = []

for n in range(N):
  start, end = map(int, input().split())
  time.append((start, end))

time.sort(key = lambda x: x[0])
time.sort(key = lambda x: x[1])

end = 0
cnt = 0

for s, e in time:
  if s >= end :
    end = e
    cnt += 1

print(cnt)