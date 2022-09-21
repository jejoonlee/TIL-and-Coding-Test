import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

dr = [0, 1]
dc = [1, 0]

for t in range(1, T + 1):

  N = int(input())
  matrix = [list(input()) for _ in range(N)]
  flag = True
  cnt = 0
  s_cnt = 0

  for row in range(N):
    if flag == False:
      break
    for column in range(N):
      if cnt == 2:
        flag = False
        break

      elif matrix[row][column] == '#':
        cnt += 1
        s_cnt += 1
        matrix[row][column] = 'X'
        queue = [(row, column)]
        queue = deque(queue)
        start = (row, column)

        while queue:
          current = queue.popleft()

          for i in range(2):
            sr = dr[i] + current[0]
            sc = dc[i] + current[1]

            if 0 <= sr < N and 0 <= sc < N:
              if matrix[sr][sc] != 'X' and matrix[sr][sc] == '#':
                matrix[sr][sc] = 'X'
                end = (sr, sc)
                queue.append((sr, sc))
                s_cnt += 1

  if flag == True and cnt == 1 and ((end[0] + 1) - start[0]) * ((end[1]+ 1) - start[1]) == s_cnt:
    print(f'#{t} yes')
  else:
    print(f'#{t} no')