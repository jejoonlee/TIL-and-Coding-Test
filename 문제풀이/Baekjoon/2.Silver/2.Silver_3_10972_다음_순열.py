
import sys
sys.stdin = open('input.txt')

N = int(input())
num = list(map(int, input().split()))

for i in range(1, N)[::-1]:
  if num[i] > num[i - 1]:
