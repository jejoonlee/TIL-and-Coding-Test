import sys
sys.stdin = open('input.txt')


T = int(input())

for _ in range(T):
  A, B = map(int, input().split())
  nums = list(map(int, input().split()))
  priority = list(set(nums))[::-1]
  cnt = 0
  index = 0

  while True:
    


  print(nums)
  print(priority)