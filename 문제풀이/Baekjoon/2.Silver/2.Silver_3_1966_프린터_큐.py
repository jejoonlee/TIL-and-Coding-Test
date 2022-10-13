import sys
sys.stdin = open('input.txt')


from collections import deque

T = int(input())

for _ in range(T):
  A, B = map(int, input().split())
  nums = deque(list(map(int, input().split())))
  priority = deque(sorted(nums, reverse=True))
  paper = deque([0] * A)
  paper[B] = 'P'

  cnt = 0


  while True:
    if paper[0] != 0 and nums[0] == priority[0]:
      cnt += 1
      break

    elif priority[0] == nums[0]:
      cnt += 1
      priority.popleft()
      nums.popleft()
      paper.popleft()
    
    elif priority[0] != nums[0]:
      nums.append(nums.popleft())
      paper.append(paper.popleft())


  print(cnt)