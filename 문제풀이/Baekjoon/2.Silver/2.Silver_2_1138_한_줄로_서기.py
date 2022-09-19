
import sys
sys.stdin = open('input.txt')

N = int(input())
height = list(range(1, N + 1))

# 해당 키의 사람이 왼쪽에 자신보다 키가 큰 사람들의 수
see = list(map(int, input().split()))

result = [0] * N

for i in range(N):
  if result[see[i]] == 0:
    result[see[i]] = height[i]
  
  elif result[see[i]] != 0:
    while True:
      see[i] += 1
      if result[see[i]] == 0:
        result[see[i]] = height[i]
        break


print(result)
print(height)
print(see)