# N X M 크기의 미로
# 1은 이동할 수 있는 칸

# 델타 탐색을 사용해서, 같은 값이 있는 방향으로 가기
# 인접 정점을 찾기

import sys
sys.stdin = open('input.txt')

# 또는 도착 위치 (n - 1, m - 1)
n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

# delta search
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 좌표를 스택에 넣어서 dfs를 한다

stack = [(0, 0)]
visited[0][0] = 1

while len(stack) != 0:
    row, column = stack.pop(0)
    # 맨 앞에 있는 것을 빼낸다

    if row == n - 1 and column == m - 1:
        break

    for i in range(4):
        sr = dr[i] + row
        sc = dc[i] + column

        if 0 <= sr < n and 0 <= sc < m:
            if visited[sr][sc] == 0 and maze[sr][sc] == 1:
                stack.append((sr, sc))
                visited[sr][sc] = visited[row][column] + 1

print(visited[n - 1][m - 1])