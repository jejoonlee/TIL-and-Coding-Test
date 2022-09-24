
import sys
sys.stdin = open('input.txt')

# ? 는 검정색 or 흰색
# ? 는 둘 다 되니깐, 코드에서 무시해도 된다
# . 은 흰색
# # 검정색
T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    board = [input() for _ in range(N)]

    answer = [0, 0, 0, 0]

    for row in range(N):
        for col in range(M):

            if board[row][col] == '.':
                if (row + col) % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
            
            elif board[row][col] == '#':
                if (row + col) % 2 == 0:
                    answer[2] += 1
                else:
                    answer[3] += 1

    if (answer[0] and answer[1]) or (answer[2] and answer[3]) or (answer[0] and answer[2]) or (answer[1] and answer[3]):
        print(f'#{t + 1} impossible')
    else:
        print(f'#{t + 1} possible')