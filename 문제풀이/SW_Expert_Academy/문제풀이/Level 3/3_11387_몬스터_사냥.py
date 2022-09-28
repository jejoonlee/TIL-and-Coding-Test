import sys
sys.stdin = open('input.txt')

# D, N, L
# D(1 + N * L%)

T = int(input())

for t in range(1, T + 1):
  D, L, N = map(int, input().split())
  result = 0

  for n in range(N):
    damage = D * (1 + n * (L / 100))
    result += damage

  print(f'#{t} {int(result)}')