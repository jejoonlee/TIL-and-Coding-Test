import sys
sys.stdin = open('input.txt')

# 1은 N극 성실, 2는 S극 성질
# S극은 밑에, N극은 위에

# 1을 기준으로 그냥 1일 계속 1씩 내리면서 탐색하기

# while문
# 1 밑에 0이 있을 경우, 1씩 내려가면서 계속 탐색을 한다
    # 그러다가 끝에 도달하면, 1을 사라지게 한다
# 1이 밑을 탐색하다, 1이 나오면 아무 상관 없어 while문을 끝낸다
# 1이 밑을 탐색하다, 2가 나오면 교착 상태의 개수를 센 후 while문을 끝낸다


for t in range(10):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for r in range(N):
        for c in range(N):
            
            if board[r][c] == 1:
                if r == (N - 1):
                    board[r][c] = 0
                else:
                    south = r
                    while south != (N - 1):
                        south += 1
                        if board[south][c] == 0:
                            if south == 6:
                                board[r][c] = 0
                        elif board[south][c] == 1:
                            break
                        elif board[south][c] == 2:
                            cnt += 1
                            break

    print(f'#{t + 1} {cnt}')