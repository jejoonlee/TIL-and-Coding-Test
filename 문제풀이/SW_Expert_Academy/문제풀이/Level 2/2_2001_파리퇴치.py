import sys
sys.stdin = open('input.txt','r')

def pprint(lst):
    for row in lst:
        print(row)

T = int(input())

for t in range(1, T + 1):

    N, M = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(N)]

    total = [[0] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):

            add = 0
            for i in range(x, x + M):
                for j in range(y, y + M):

                    if 0 <= i < N and 0 <= j < N:
                        add += area[i][j]
                    
            total[x][y] = add

    max_num = 0
    for x in range(N):
        for y in range(N):
            if total[x][y] > max_num:
                max_num = total[x][y]

    print(f'#{t} {max_num}')