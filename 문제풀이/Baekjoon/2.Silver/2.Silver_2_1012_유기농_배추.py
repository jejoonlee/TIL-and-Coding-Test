import sys
sys.stdin = open('input.txt')

# 상하좌우 네 방향으로 배추를 보호할 수 있음
# 필요한 배추흰지렁이의 개수를 구하는 것
def pprint(lst):
    for pr in lst:
        print(pr)

T = int(input())

# 델타 탐색, 위 왼 오 아
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

for _ in range(T):
    
    # M = 가로길이 / N = 세로길이 / K 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())

    # 배추 심을 land를 만들어준다 
    land = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 배추 심어주기
    for i in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1

    cnt = 0
    for r in range(N):
        for c in range(M):

            # DFS 시작 기준은, land 이차원 리스트를 순회하면서 land의 값이 1이거나
            # 방문을 안 한 곳
            if land[r][c] == 1 and visited[r][c] == False:
                # DFS가 시작할때마다 cnt에 1을 누적시킨다
                cnt += 1
                stack = [(r, c)]
                visited[r][c] = True

                while len(stack) != 0:
                    current = stack.pop()

                    for i in range(4):
                        sr = current[0] + dr[i]
                        sc = current[1] + dc[i]
                    
                        if 0 <= sr < N and 0 <= sc < M:
                            if land[sr][sc] == 1 and visited[sr][sc] == False:
                                visited[sr][sc] = True
                                stack.append((sr, sc))
    print(cnt)