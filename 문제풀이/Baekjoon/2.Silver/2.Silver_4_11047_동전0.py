import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

coins = []
for _ in range(N):
  coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for i in coins:
  if K >= i:
    cnt += K // i
    K -= i * (K // i)

    if K == 0:
      break

print(cnt)