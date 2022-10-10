import sys
sys.stdin = open('input.txt')

# 적록색약은 빨간색과 초록색을 한 색깔로 같이 본다

N = int(input())
colors = [list(input()) for _ in range(N)]

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def dfs(row, col):
  stack = [(row, col)]

  while stack:
    now = stack.pop()

    for i in range(4):
      sr = dr[i] + now[0]
      sc = dc[i] + now[1]

      if 0 <= sr < N and 0 <= sc < N:
        if colors[sr][sc] == color:
          if color == 'B':
            colors[sr][sc] = 'v'
            stack.append((sr,sc))
          elif color == 'G' or color == 'R':
            colors[sr][sc] = 'h'
            stack.append((sr,sc))
          elif color == 'h':
            colors[sr][sc] = 'visited'
            stack.append((sr,sc))
          elif color == 'v':
            colors[sr][sc] = 'visited'
            stack.append((sr,sc))

cnt = [0, 0]


for row in range(N):
  for col in range(N):
    
    if colors[row][col] == 'B':
      color = 'B'
      colors[row][col] = 'v'
      cnt[0] += 1

      dfs(row,col)

    elif colors[row][col] == 'R':
      color = 'R'
      colors[row][col] = 'h'
      cnt[0] += 1

      dfs(row, col)

    elif colors[row][col] == 'G':
      color = 'G'
      colors[row][col] = 'h'
      cnt[0] += 1

      dfs(row, col)

for row in range(N):
  for col in range(N):
    if colors[row][col] == 'v':
      color = 'v'
      colors[row][col] = 'visited'
      cnt[1] += 1

      dfs(row, col)

    elif colors[row][col] == 'h':
      color = 'h'
      colors[row][col] = 'visited'
      cnt[1] += 1

      dfs(row, col)

print(' '.join(map(str, cnt)))