import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  N, K = map(int, input().split())

  min_ = N // K
  max_ = (N // K) + (N % K)

  print(f'#{t} {max_ - min_}')
