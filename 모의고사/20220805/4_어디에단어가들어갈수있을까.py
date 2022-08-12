import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 연속으로 k번을 가면 + 1
# k번보다 작거나 크면 0

T = int(input())

for t in range(1, T + 1):

    # 퍼즐 가로, 세로 / 단어 길이
    N , K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    row = 0
    # 퍼즐은 정사각현
    for i in range(N):
        cnt = 0
        for j in range(len(puzzle)):
            if puzzle[i][j] == 1:
                cnt += 1
            elif puzzle[i][j] == 0 and cnt == K:
                row += 1
                cnt = 0
            elif puzzle[i][j] == 0:
                cnt = 0
        if cnt == K:
            row += 1
            cnt = 0

    col = 0
    for i in range(N):
        cnt = 0    
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            elif puzzle[j][i] == 0 and cnt == K:
                col += 1
                cnt = 0
            elif puzzle[j][i] == 0:
                cnt = 0
        if cnt == K:
            col += 1
            cnt = 0

    print(f'#{t} {row + col}')