import sys
sys.stdin = open('input.txt')

# N : 농부가 키우는 소의 수
# S : 코스튬에 들어갈 수 있는 2마리의 소 사이즈
N, S = map(int, input().split())
cnt = 0

cows = []
for _ in range(N):
  cows.append(int(input()))


for i in range(0, N):
  j = i
  while j != N - 1:
    j += 1
    if cows[i] + cows[j] <= S:
      cnt += 1

print(cnt)