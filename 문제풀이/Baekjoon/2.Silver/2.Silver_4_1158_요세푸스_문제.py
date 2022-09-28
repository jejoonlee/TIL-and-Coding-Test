import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, input().split())
cnt = 0

nums = []
for i in range(1, N + 1):
  nums.append(i)

nums = deque(nums)

result = []

while nums:
  cnt += 1
  if cnt != K:
    temp = nums.popleft()
    nums.append(temp)

  else:
    result.append(nums.popleft())
    cnt = 0

result = ', '.join(map(str, result))
print(f'<{result}>')