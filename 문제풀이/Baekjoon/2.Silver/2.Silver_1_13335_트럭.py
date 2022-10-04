import sys
sys.stdin = open('input.txt')

from collections import deque

n, w, L = map(int, input().split())

trucks = deque(list(map(int, input().split())))

queue = deque([0] * w)
cnt = 0
weight = 0

while True:
  if trucks:
    truck = trucks.popleft()
    weight += truck

    if weight <= L:
      queue.popleft()
      queue.append(truck)
      cnt += 1
    
    else:
      while True:
        queue.popleft()
        queue.append(0)
        cnt += 1

        if sum(queue) + truck <= L:
          queue.popleft()
          queue.append(truck)
          weight = 0
          break
  
  else:
    while True:
      queue.popleft()
      queue.append(0)
      cnt += 1

      if sum(queue) == 0:
        queue.popleft()
        queue.append(0)
        weight = 0
        break
    break

print(cnt)