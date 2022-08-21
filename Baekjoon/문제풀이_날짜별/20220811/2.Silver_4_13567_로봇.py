import sys
sys.stdin = open('input.txt', 'r')

def pprint(lst):
    for row in lst:
        print(row)

# m은 정사각형 한 변의 길이, n는 명령어 수
M, n = map(int, input().split())

area = [[0] * (M + 1) for _ in range(M + 1)]

            # 오른쪽, 위, 왼쪽, 아래
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            # 움직일 때에, 움직이는 수 만큼 곱해주면 된다!

# start row / start column
start_row, start_column = M, 0

# 스타트 포인트
area[start_row][start_column] = 'R'

dir = 0
# 방향은 인덱스로 가지고 오면 된다. 즉 dir의 최대 수는 3이다

for _ in range(n):
    flag = True
    com = input().split()

    # 회전하는 경우를 넣은다
    if com[0] == 'TURN':
        if com[1] == '0':
                dir += 1                
                # 방향은 4 방향 밖에 없다.
                # 즉 방향이 4가 되면, 0으로 초기화 시킨다
                if dir == 4:
                    dir = 0
        elif com[1] == '1':
                dir -= 1
                if dir == -4:
                    dir = 0

    elif com[0] == 'MOVE':
        move_dir = directions[dir]
        # 행과 열로 얼마나 어느 방향으로 움직이는지 계산을 한다
        row_move, column_move =  move_dir[0] * int(com[1]), move_dir[1] * int(com[1])

        mr = start_row + row_move
        mc = start_column + column_move

        if not(0 <= mr < (M + 1) and 0 <= mc < (M + 1)):
            print(-1)
            flag = False
            break

        # 안으로 움직였으면 원래 있는 값은 0으로 변환
        else:
            area[start_row][start_column] = 0
            area[mr][mc] = 'R'
            # 움직인 것을 좌표에 넣고, 그전 좌표값을 지금 좌표값으로 바꾼다
            start_row, start_column = mr, mc

# 지금까지 좌표값은 행과 열
# x, y 좌표값으로 바꿔준다
if flag == True:
    x = mc
    y = M - mr
    print(x, y)