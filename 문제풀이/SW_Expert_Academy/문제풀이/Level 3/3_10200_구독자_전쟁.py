import sys
sys.stdin = open('input.txt')

T = int(input())

# N, A, B 가 입력값
# 주어진 값 중 작은 값이 최대값이 된다

# A + B > N 일때
  # 최소값은 (A+B) - N
# A + B <= N 일때
  # 최고값은 0

for t in range(1, T + 1):
  N, A, B = map(int, input().split())
  max_min = [0,0]

  max_min[0] = min(A, B)

  if A + B > N:
    max_min[1] = (A + B) - N
  else:
    max_min[1] = 0

  print(f"#{t} {' '.join(map(str,(max_min)))}")