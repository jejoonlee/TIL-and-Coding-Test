# 델타 이동 / 델타 탐색
# 한 데이터 기준으로 '상하좌우'를 탐색
# 상 y = y - 1 / 하 y = y + 1 / 좌 x = x - 1/ 우 x = x + 1

# 탐색을 한 후 지뢰가 있으면, 지뢰 수에 1을 누적한다

import sys
sys.stdin = open('input.txt', 'r')

def pprint(list_):
    for row in list_:
        print(row)


N = int(input())

mine_field = [list(input()) for _ in range(N)]
sel = [list(input()) for _ in range(N)]
ans = [['.'] * N for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
dy = [-1, 0, 1, -1, 1, -1, 0, 1] 


# 이차원 리스트 순회
for x in range(N):
    for y in range(N):
        
        bomb = 0
        # 순회하는데 x가 있을 때에
        if mine_field[x][y] == '.' and sel[x][y] == 'x':
        
            #델타 탐색 8면
            for i in range(8):
                sx = dx[i] + x
                sy = dy [i] + y

                # 델타 탐색이 범위 내에 있고
                # 주변에 지뢰가 있으면 bomb에 1을 더하기
                if 0 <= sx < N and 0 <= sy < N:
                    if mine_field[sx][sy] == '*':
                        bomb += 1
            ans[x][y] = bomb

        if mine_field[x][y] == '*' and sel[x][y] == 'x':
            for a in range(N):
                for b in range(N):
                    if mine_field[a][b] == '*':
                        ans[a][b] = '*'

for i in range(N):
    for j in range(N):
        print(ans[i][j], end = '')
    print()