import sys
sys.stdin = open('input.txt')

# 주어진 단어 만큼 딱 맞게 공간에 들어가야 한다
# 가로랑 세로로 총 몇개의 단어가 들어갈 수 있는지 계산해야 한다
# 1이 빈 공간 0이 막힌 공간

def pprint(lst):
    for i in lst:
        print(i)

T = int(input())

for t in range(1, T + 1):
    # N은 가로, 세로 길이 / K는 단어의 길이
    N, K = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(N)]

    row = 0
    row_cnt = 0
    column_cnt = 0

    for r in range(N):
        row = 0
        for c in range(N):

            if area[r][c] == 0:
                row = 0
                continue
            else:
                row += 1
                
                if row == K:
                    if (0 <= c + 1 < N and area[r][c + 1] == 0) or not(0 <= c + 1 < N):
                        row_cnt += 1
                        row = 0
    
    cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):

            if area[j][i] == 0:
                cnt = 0
                continue
            else:
                cnt += 1

                if cnt == K:
                    if (0 <= j + 1 < N and area[j + 1][i] == 0) or not(0 <= j + 1 < N):
                        column_cnt += 1
                        cnt = 0

    print(f'#{t} {row_cnt + column_cnt}')