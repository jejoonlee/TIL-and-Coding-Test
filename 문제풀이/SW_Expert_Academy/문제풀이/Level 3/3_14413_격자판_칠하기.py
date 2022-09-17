
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
    flag = True

    for r in range(N):
        if flag == False:
            break
        
        for c in range(M):
            if c + 1 < M and r + 1 < N and board[r][c] == '#':
                if board[r][c + 1] == '#':
                    print(f'#{t+1} impossible')
                    flag = False
                    break
            
            if c + 1 < M and board[r][c] == '.':
                if board[r][c + 1] == '.':
                    print(f'#{t+1} impossible')
                    flag = False
                    break

    if flag == True:
        print(f'#{t+1} possible')