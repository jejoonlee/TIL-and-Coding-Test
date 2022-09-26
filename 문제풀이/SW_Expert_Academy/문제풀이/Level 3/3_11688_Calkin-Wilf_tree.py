
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  direc = input()
  a, b = 1, 1

  for d in direc:

    if d == 'L':
      b += a

    else:
      a += b

  print(f'#{t} {a} {b}')