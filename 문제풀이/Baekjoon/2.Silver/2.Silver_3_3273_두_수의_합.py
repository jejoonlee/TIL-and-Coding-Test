import sys
sys.stdin = open('input.txt')

n = int(input())
array = list(map(int, input().split()))
x = int(input())

cnt = 0

for i in range(n-1):
  j = i
  
  while j != n-1:
    j += 1
    if array[i] + array[j] == x:
      cnt += 1

print(cnt)