import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  N = int(input())
  income = list(map(int, input().split()))
  cnt = 0

  avg = sum(income) / N

  for n in income:
    if n <= avg:
      cnt += 1

  print(f'#{t} {cnt}')