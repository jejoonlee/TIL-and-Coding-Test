import sys
sys.stdin = open('input.txt')

import sys
N, M = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
num = 0

for i in array:
  num += i
  prefix_sum.append(num)

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  print(prefix_sum[j] - prefix_sum[i - 1])