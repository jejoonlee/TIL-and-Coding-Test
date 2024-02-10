
import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

idx, count = 0, 0

while k > 0:
    if coins[idx] <= k:
        count += k // coins[idx]
        k = k % coins[idx]
    idx += 1

print(count)