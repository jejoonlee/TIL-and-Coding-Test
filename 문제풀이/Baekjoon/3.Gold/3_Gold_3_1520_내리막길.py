import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("input.txt")

def move(row, column):

    # Base code: 재귀를 빠져 나오는 것
    if row == N - 1 and column == M - 1:
        return 1

    # 방문을 하지 않았으면, 계속 탐색하는 것
    if visited[row][column] == -1:
        visited[row][column] = 0

        for i in range(4):
            sr, sc = dr[i] + row, dc[i] + column

            if 0 <= sr < N and 0 <= sc < M:
                if matrix[row][column] > matrix[sr][sc]:

                    # 만약 끝까지 갔다면, move(sr,sc)는 1을 출력
                    visited[row][column] += move(sr, sc)

    # 방문을 한 곳이면, 해당 좌표의 숫자를 출력한다
    # 숫자는 몇 개의 경로를 탐색했는지 알려준다
    # 결국에는 콜스택이 다 없어지면서, visited[0][0]을 출력해준다
    return visited[row][column]

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]

print(move(0,0))
print(visited)