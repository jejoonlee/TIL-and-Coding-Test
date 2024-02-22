import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split(' ')) 

dir = [[-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [1, 0, 0]]

def bfs(queue):

    global box
    count = -1

    while queue:

        count += 1

        for _ in range(len(queue)):
            height, row, column = queue.popleft()

            for i in range(6):
                sh, sr, sc = dir[i][0] + height, dir[i][1] + row, dir[i][2] + column

                if 0 <= sh < h and 0 <= sr < m and 0 <= sc < n:
                    if box[sh][sr][sc] == 0:
                        queue.append([sh, sr, sc])
                        box[sh][sr][sc] = 2

    return count


box = []
queue = deque()

for i in range(h):
    box.append([])
    for j in range(m):
        box[i].append(list(map(int, input().split(' '))))

for i in range(h):
    for j in range(m):
        for k in range(n):
            if box[i][j][k] == 1: queue.append([i, j, k])

count = bfs(queue)

flag = True

for i in range(h):
    if not flag: break
    for j in range(m):
        if not flag: break
        for k in range(n):
            if box[i][j][k] == 0:
                flag = False
                print(-1)
                break

if flag: print(count)
