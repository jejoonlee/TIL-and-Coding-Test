import sys
sys.stdin = open('input.txt')

# D, N, L
# D(1 + N * L%)

T = int(input())

for t in range(1, T + 1):
  D, L, N = map(int, input().split())

  result = D * (1 + L * (N * 1/100))

  print(f'#{t} {result}')