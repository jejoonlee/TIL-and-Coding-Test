import sys
sys.stdin = open('input.txt')

N = int(input())

meetings = []
for _ in range(N):
  a, b = map(int, input().split())
  meetings.append((a,b))

meetings.sort()

result = []
for i in range(N - 1):
  cnt = 0
  j = i + 1
  while j != N - 1:
    if meetings[i][1] <= meetings[j][0]:
      cnt += 1
      i = j
      j = i
    else:
      j += 1
  
  result.append(cnt)

print(result)