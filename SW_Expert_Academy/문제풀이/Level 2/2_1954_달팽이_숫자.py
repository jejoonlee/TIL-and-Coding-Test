import sys
sys.stdin = open('input.txt')

# 순회를 하면서, 벽이 있거나, 0이 아닐 경우 방향을 바꾼다
# 기본적인 방향은 오른쪽 / 아래 / 왼쪽 / 위
# 그렇게 델타 탐색이 끝나면
# 다시 이차원 리스트를 순회를 하며, 0을 찾는다
# 0을 찾게되면, 다시 델타 탐색을 오른쪽 / 아래 / 왼쪽 / 위 를 돈다

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]

    # 오른쪽, 아래, 왼쪽, 위
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cnt = 0
    for r in range(N):
        for c in range(N):
            
            if matrix[r][c] == 0:
                cnt += 1
                matrix[r][c] = cnt

                for i in range(4):
                    sr = r + dr[i]
                    sc = c + dc[i]

                    while True:
                        if 0 <= sr < N and 0 <= sc < N:
                            if not(matrix[sr][sc] == 0):
                                r = sr - dr[i]
                                c = sc - dc[i]
                                break
                            else:
                                cnt += 1
                                matrix[sr][sc] = cnt
                                sr += dr[i]
                                sc += dc[i]
                        else:
                            r = sr - dr[i]
                            c = sc - dc[i]
                            break
    
    print(f'#{t}')    
    for i in matrix:
        print(*i)