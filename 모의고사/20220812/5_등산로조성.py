# import sys

# sys.stdin = open("_등산로조성.txt")

import sys

sys.stdin = open("input.txt")

# 출발점은 가장 높은 봉우리
# 위, 아래, 오른쪽, 왼쪽 델타 탐색
# 한 곳의 지형을 깎을 수 있음....
# 최대한 긴 길이의 값

# 위 왼쪽, 오른쪽, 아래
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# N = 지도 크기 / K 최대 공사 깊이
N, K = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        visited = [[False] * N for _ in range(N)]

        # 델타탐색
        for a in range(4):
            nr = dr[a] + r
            nc = dc[a] + c

            if 0 <= nr < N and 0 <= nc < N:
                if area[r][c] > area[nr][nc]:
                    visited[r][c] = True
                    stack = [(nr, nc)]
                    
                    # dfs를 할 때에, 더 작은 값들을 찾기
                    while len(stack) != 0:
                        c_row, c_column = stack.pop()

                        for b in range(4):
                            sr = dr[b] + c_row
                            sc = dc[b] + c_column

                            if 0 <= sr < N and 0 <= sc < N:
                                if area[sr][sc] < area[c_row][c_column]:
                                    if not visited[c_row][c_column]:
                                        visited[c_row][c_column] = True
                                        stack.append((sr, sc))
