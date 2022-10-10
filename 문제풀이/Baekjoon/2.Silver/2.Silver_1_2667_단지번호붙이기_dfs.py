import sys
sys.stdin = open('input.txt')

# 단지 개수를 구하고 / 단지에 속하는 집의 수를 오름차순으로 정렬해서 출력

N = int(input())

map = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

# 델타 탐색
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

block_cnt = 0

house = []
for r in range(N):
    for c in range(N):

        if map[r][c] == 1 and visited[r][c] == False:
            block_cnt += 1
            house_cnt = 1
            visited[r][c] = True
            stack = [(r, c)]

            while len(stack) != 0:
                cur = stack.pop()

                for i in range(4):
                    sr = cur[0] + dr[i]
                    sc = cur[1] + dc[i]

                    if 0 <= sr < N and 0 <= sc < N:
                        if map[sr][sc] == 1 and visited[sr][sc] == False:
                            stack.append((sr, sc))
                            visited[sr][sc] = True
                            house_cnt += 1
            house.append(house_cnt)

house.sort()

print(block_cnt)
for h in house:
    print(h)