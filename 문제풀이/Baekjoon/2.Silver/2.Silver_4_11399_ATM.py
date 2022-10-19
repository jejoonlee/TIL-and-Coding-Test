import sys
sys.stdin = open('input.txt')

N = int(input())
P = list(map(int,input().split()))

# 주어진 입력값에서 오름차순으로 정렬을 하게되면
# 최소 값을 얻을 수 있다
P.sort()

add_ = 0
result = 0

for p in range(N):
  add_ += P[p]
  result += add_

print(result)