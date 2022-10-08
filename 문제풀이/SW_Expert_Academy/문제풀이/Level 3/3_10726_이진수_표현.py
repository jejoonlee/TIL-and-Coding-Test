import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  N, M = map(int, input().split())

  flag = True

  for _ in range(N):
    if M % 2 == 1:
      M //= 2
      continue
    else:
      flag = False
      print(f'#{t} OFF')
      break
  
  if flag == True:
    print(f'#{t} ON')