# 1 이 연결된 것이 하나의 그림이다 (가로, 세로)
# 그림의 개수와 제일 큰 그림 구하기
import sys
sys.stdin = open('input.txt')


# 세로, 가로 크기
n, m = map(int, input().split())

portrait = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# delta 탐색 (4면)
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

portrait_size = []

for row in range(n):
    for column in range(m):

        if portrait[row][column] == 1 and visited[row][column] == False:
            stack = [(row, column)]
            visited[row][column] = True

            size_cnt = 1

            while stack:
                r, c = stack.pop()

                for i in range(4):
                    sr = r + dr[i]
                    sc = c + dc[i]

                    if 0 <= sr < n and 0 <= sc < m:
                        if visited[sr][sc] == False and portrait[sr][sc] == 1:
                            stack.append((sr, sc))
                            visited[sr][sc] = True
                            size_cnt += 1
        
            portrait_size.append(size_cnt)

if len(portrait_size) == 0:
    print(len(portrait_size))
    print(0)
else:
    print(len(portrait_size))
    print(max(portrait_size))