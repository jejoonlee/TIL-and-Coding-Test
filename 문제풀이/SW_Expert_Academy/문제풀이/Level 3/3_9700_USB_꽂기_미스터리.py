# 문제에서 p 에 관련된 내용은, '처음에' 정우가 USB를 가지고 있는 상태를 말한다
  # 제대로 된 면에서 USB를 가지고 있을 확률이 p
  # 반대가 1-p
  # p는 한번만 생각하면 됨

# 한번 뒤집고 성공 (1-p)로 시작
# 두번일 경우
  # O X O - 처음에 올바른 면을 가지고 있고, 실패를 했다 가정 후 2번 뒤집기
  # X O X - 처음에 반대쪽 면으로 시작하면, 마지막 2번째 뒤집었을 때 절대로 성공 X

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
  p, q = map(float, input().split())

  s1 = (1-p) * q
  s2 = p * (1-q) * q

  if s1 < s2:
    print(f'#{t} YES')
  else:
    print(f'#{t} NO')