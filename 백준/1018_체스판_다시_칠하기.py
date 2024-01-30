
n, m = map(int, input().split(' '))

board = [list(input()) for _ in range(n)]


answer = 8 * 8

for i in range(0, n - 8 + 1):
    
    for j in range(0, m - 8 + 1):

        # W가 짝수일 때, W가 홀수일 때
        caseOne, caseTwo = 0, 0

        for k in range(i, i + 8):

            for l in range(j, j + 8):

                if (k + l) % 2 == 0:

                    if board[k][l] == 'W':
                        caseTwo += 1
                    elif board[k][l] == 'B':
                        caseOne += 1
                
                else:
                    if board[k][l] == 'W':
                        caseOne += 1
                    elif board[k][l] == 'B':
                        caseTwo += 1

        answer = min(caseOne, caseTwo, answer)

print(answer)