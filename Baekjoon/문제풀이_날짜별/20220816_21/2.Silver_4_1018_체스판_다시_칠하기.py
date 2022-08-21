import sys
sys.stdin = open('input.txt')


M, N = map(int, input().split())

board = [list(input()) for _ in range(M)]

cnt_lst = []

# 탐색을 두번 한다
# 먼저 큰 행열에 이중 for문을 넣는다
for row in range(M - 7):
    for column in range(N - 7):

        # 무조건 [row][column]이 검정이라고, 검정으로 시작 안 해도 된다
        cnt_1, cnt_2 = 0, 0

        # 8 * 8 chess판을 비교하는 것으로, 작게 for문을 돈다
        # 그리고 조건문에 따라 결과가 나오게 한다
        for r in range(row, row + 8):
            for c in range(column, column + 8):

                if 0 <= r < M and 0 <= c < N:
                    # 짝수가 흰색이어야 할 경우,
                    # 짝수에 검정, 그리고 홀수에 흰색이 있으면 1을 누적시킨다
                    if (r + c) % 2 == 0 and board[r][c] != 'W':
                        cnt_1 += 1
                    if (r + c) % 2 == 1 and board[r][c] != 'B':
                        cnt_1 += 1
                    
                    # 짝수가 검정이어야 할 경우
                    # 짝수에 흰색, 그리고 홀수에 검정이 있으면 1을 누적시킨다
                    if (r + c) % 2 == 0 and board[r][c] != 'B':
                        cnt_2 += 1
                    if (r + c) % 2 == 1 and board[r][c] != 'W':
                        cnt_2 += 1

        cnt_lst.append(min(cnt_1, cnt_2))

print(min(cnt_lst))