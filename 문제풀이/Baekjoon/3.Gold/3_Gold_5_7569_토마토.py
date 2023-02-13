import sys
sys.stdin = open("input.txt")

from collections import deque

def bfs(queue):

    while queue:
        current_h, current_r, current_c = queue.popleft()

        for i in range(6):
            sh, sr, sc = current_h + dh[i], current_r + dr[i], current_c + dc[i]

            if 0 <= sr < N and 0 <= sc < M and 0 <= sh < H:
                if box[sh][sr][sc] == 0 and box[sh][sr][sc] != -1:
                    box[sh][sr][sc] = box[current_h][current_r][current_c] + 1
                    queue.append((sh, sr, sc))

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque([])

# 북서동남, 위 아래
dh, dr, dc= [0, 0, 0, 0, -1, 1], [-1, 0, 0, 1, 0, 0], [0, -1, 1, 0, 0, 0]

answer = 0

# queue에다 시작 점들 넣기
for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1:
                queue.append((h, r, c))

bfs(queue)

flag = True
for h in range(H):
    if flag == False:
        break
    for r in range(N):
        if flag == False:
            break
        for c in range(M):
            if box[h][r][c] == 0:
                flag = False
                break
                
        answer = max(answer, max(box[h][r]))

if flag == False:
    print(-1)
else:
    print(answer -1)