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

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
print(time)
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
print(time)

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  print(i, j)
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)