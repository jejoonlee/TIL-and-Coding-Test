import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

nums = list(map(int, input().split(' ')))

numAdd = [0] * (n + 1)

for i in range(n): numAdd[i + 1] = nums[i] + numAdd[i]

for _ in range(m):
    i, j = map(int, input().split(' '))

    print(numAdd[j] - numAdd[i - 1])