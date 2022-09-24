
# 입력 값들을 리스트에 정수로 저장한다
# 리스트에 있는 요소들의 개수를 3으로 나눈다
  # 그러면 몇 개 그룹이 나온지 알 수 있다
# 내림차순으로 정수를 정렬한다
  # 인덱스 중 3이랑 나눴을 때 2로 나누어 떨어지는 숫자들을 모두 제외하고
  # 더한 값이 정답

import sys
sys.stdin = open('input.txt') 

N = int(input())

# purchase = []
# for _ in range(N):
#   C = int(input())
#   purchase.append(C)

purchase = [int(input()) for _ in range(N)]

purchase.sort(reverse = True)
result = 0

for p in range(N):
  if not(p % 3 == 2):
    result += purchase[p]

print(result)