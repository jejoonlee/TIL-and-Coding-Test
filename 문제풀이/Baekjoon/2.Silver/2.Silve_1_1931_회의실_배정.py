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

input = sys.stdin.readline

N = int(input())

meeting = []
for n in range(N):
  a, b = map(int, input().split())
  meeting.append((a,b))

meeting.sort()

result = 0
for m in range(N - 1):

  cnt = 1
  n = m + 1

  while n != N:
    
    if meeting[m][1] <= meeting[n][0]:
      m = n
      n = m + 1
      cnt += 1
    
    else:
      n += 1
  
  if result < cnt:
    result = cnt

print(result)