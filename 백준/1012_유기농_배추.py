import sys
from collections import deque


dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        current = queue.popleft()

        for i in range(4):
            sr, sc = current[0] + dir[i][0], current[1] + dir[i][1]

            if 0 <= sr < n and 0 <= sc < m:
                if field[sr][sc] == 1:
                    field[sr][sc] = 2
                    queue.append([sr, sc])


t = int(input())

for _ in range(t):

    m, n, k = map(int, input().split(" "))

    field = [[0] * m for _ in range(n)]

    count = 0

    for _ in range(k):
        c, r = map(int, input().split())
        field[r][c] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                count += 1
                bfs(i, j)

    print(count)