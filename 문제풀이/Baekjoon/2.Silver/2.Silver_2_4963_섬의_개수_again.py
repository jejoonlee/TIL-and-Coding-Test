
import sys
sys.stdin = open('input.txt')

from collections import deque

# 델타 탐색
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(row, column):

  queue = [(row,column)]
  queue = deque(queue)

  while queue:
    current = queue.popleft()

    # 델타 탐색
    for i in range(8):
      sr = dr[i] + current[0]
      sc = dc[i] + current[1]

      if 0 <= sr < h and 0 <= sc < w:
        if land[sr][sc] == 1 and visited[sr][sc] == False:
          visited[sr][sc] = True
          queue.append((sr, sc))


while True:

  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  land = [list(map(int, input().split())) for _ in range(h)]
  visited = [[False] * w for _ in range(h)]

  cnt = 0

  for row in range(h):
    for column in range(w):

      if land[row][column] == 1 and visited[row][column] == False:
        
        visited[row][column] = True
        cnt += 1
        
        bfs(row, column)

  print(cnt)