import sys
sys.stdin = open('input.txt')


from collections import deque

N, M = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]


queue = deque([(0, 0)])
visited[0][0] = 1

while queue:
    row, column = queue.popleft()

    for i in range(4):
        sr, sc = row + dr[i], column + dc[i]

        if 0 <= sr < N and 0 <= sc < M:
            if matrix[sr][sc] == 1 and visited[sr][sc] == 0:
                visited[sr][sc] = visited[row][column] + 1
                queue.append((sr, sc))
            

print(visited[N-1][M-1])