import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  N = int(input())
  flag = True

  for i in range (1, 10):
    temp = N / i
    left = N % i

    if temp // 10 == 0 and left == 0:
      flag = True
      break

    else:
      flag = False

  if flag == True:
    print(f'#{t} Yes')
  else:
    print(f'#{t} No')