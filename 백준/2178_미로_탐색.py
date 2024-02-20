import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(' '))

maze = [input().strip() for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def bfs():
    queue = deque()
    queue.append([0,0])

    while queue:
        current = queue.popleft()

        for i in range(4):
            sr = dir[i][0] + current[0]
            sc = dir[i][1] + current[1]

            if 0 <= sr < n and 0 <= sc < m:
                if maze[sr][sc] == '1':
                    if visited[sr][sc] == 0 or visited[sr][sc] > visited[current[0]][current[1]] + 1:
                        visited[sr][sc] = visited[current[0]][current[1]] + 1
                        queue.append([sr, sc])

bfs()

print(visited[n - 1][m - 1])
