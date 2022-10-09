import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
  A, B = map(int, input().split())
  nums = []
  cnt = 0
  result = 0

  for num in range(A, B+1):
    if str(num) == str(num)[::-1]:
      nums.append(num)

  while True:
    cnt += 1

    if str(cnt) == str(cnt)[::-1]:
      if cnt ** 2 in nums:
        result += 1
        continue
      elif cnt ** 2 > B:
        break

  print(f'#{t} {result}')