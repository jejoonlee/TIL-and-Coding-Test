import sys
sys.stdin = open('input.txt')

from collections import deque

n, w, L = map(int, input().split())

trucks = deque(list(map(int, input().split())))

queue = deque([0] * w)
cnt = 0
weight = 0

while queue:
  cnt += 1

  if trucks:
    weight -= queue.popleft()
    if weight + trucks[0] <= L:
      weight += trucks[0]
      queue.append(trucks.popleft())

    else:
      queue.append(0)

  else:
    queue.popleft()

print(cnt)


# queue가 계속 밀리는 것
# 만약 트럭들이 최대 하중을 넘지 않으면 queue 안에 트럭을 추가하고
# 최대 하중을 넘으면 queue에 0을 추가해준다
# truck이 다 빠지면 queue도 순차적으로 없어지게 된다

# 최종적으로 queue에 아무것도 없을때까지 while문을 반복
# ---------------------------------------------------------------
# 시간 초과
# while queue:
#   cnt += 1
#   if trucks:
#     # 만약 트럭들이 최대 하중을 넘지 않으면 queue 안에 트럭을 추가하고
#     if weight + trucks[0] <= L:
#       weight += trucks[0]
#       queue.append(trucks.popleft())
#       queue.popleft()

#     # 최대 하중을 넘으면 queue에 0을 추가해준다
#     else:
#       queue.append(0)
#       out = queue.popleft()
#       weight -= out

#       if weight + trucks[0] <= L:
#         weight += trucks[0]
#         queue.append(trucks.popleft())
#         queue.popleft()
  
#   else:
#     queue.popleft()

# print(cnt)