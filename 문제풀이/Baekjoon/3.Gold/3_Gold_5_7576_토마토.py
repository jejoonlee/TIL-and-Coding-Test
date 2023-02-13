import sys
sys.stdin = open("input.txt")

from collections import deque


def bfs(queue):
    dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]


    while queue:
        r, c = queue.popleft()

        for i in range(4):
            sr, sc = dr[i] + r, dc[i] + c

            if 0 <= sr < m and 0 <= sc < n:
                if box[sr][sc] != -1 and box[sr][sc] == 0:
                    queue.append((sr, sc))
                    box[sr][sc] = box[r][c] + 1


n, m = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(m)]

queue = deque([])

answer = 0

# 시작 점들을 queue에다가 넣는다
# 시작 점들이 1개 이상일 수 있음
for i in range(m):
    for j in range(n):

        if box[i][j] == 1:
            queue.append((i, j))

bfs(queue)

flag = True
for l in range(m):
    if flag == False:
        break
    for k in range(n):
        if box[l][k] == 0:
            flag = False
            break
    
    answer = max(answer, max(box[l]))

if flag == False:
    print(-1)
else:
    print(answer - 1)