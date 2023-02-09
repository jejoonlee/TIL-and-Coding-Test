import sys
sys.stdin = open("input.txt")


def dfs(row, column, count):
    global answer

    visited.add(graph[row][column])
    answer = max(answer, count)

    for i in range(4):
        sr = dr[i] + row
        sc = dc[i] + column

        if 0 <= sr < N and 0 <= sc < M:
            if graph[sr][sc] not in visited:
                dfs(sr, sc, count + 1)

    visited.remove(graph[row][column])

    return answer

    
N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]
visited = set()

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

answer = 0

print(dfs(0, 0, 1))