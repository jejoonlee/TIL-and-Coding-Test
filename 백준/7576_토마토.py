import sys
from collections import deque

input = sys.stdin.readline

dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def bfs(queue):

    global dir, box

    count = -1

    while queue:

        count += 1

        for _ in range(len(queue)):
            curRow, curColumn = queue.popleft()

            for i in range(4):
                sr, sc = dir[i][0] + curRow, dir[i][1] + curColumn

                if 0 <= sr < m and 0 <= sc < n:
                    if box[sr][sc] == 0:
                        box[sr][sc] = 2
                        queue.append([sr, sc])
    return count


n, m = map(int, input().split(' '))

box = [list(map(int, input().split(' '))) for _ in range(m)]

queue = deque()

for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            queue.append([i, j])

count = bfs(queue)

flag = True

for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            flag = False
            print(-1)
            break
    if flag == False:
        break

if flag:
    print(count)