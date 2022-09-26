import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  A, B = map(int, input().split())

  if A < 10 and B < 10:
    print(f'#{t} {A * B}')
  else:
    print(f'#{t} -1')