import sys
sys.stdin = open('input.txt')

from collections import deque

n, w, L = map(int, input().split())

trucks = deque(list(map(int, input().split())))

queue = deque([0] * w)
cnt = 0
weight = 0

while True:
  weight += trucks[0]

  if weight <= L:
    queue.append(trucks[0])
    queue.popleft()
    trucks.popleft()

  else:
    while True:
      out = queue.popleft()
      queue.append(0)

      if trucks:
        if sum(queue) + trucks[0] > L:
          queue.popleft()
          queue.append(0)
        
        else:
          if weight - out + trucks[0] <= L:
            weight = weight - out
            break



  


print(cnt)