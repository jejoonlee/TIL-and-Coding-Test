import sys
sys.stdin = open('input.txt')

# 이거 그냥... 3으로 나누면 되잖아...

T = int(input())

for t in range(1, T + 1):
  student = int(input())
  print(f'#{t} {student // 3}')