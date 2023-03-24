import sys
sys.stdin = open('input.txt')

N = int(input())

stairs = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    stairs[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            stairs[i][j] = stairs[i-1][j + 1]
        
        elif 0 < j < 9:
            stairs[i][j] = stairs[i-1][j+1] + stairs[i-1][j-1]

        elif j == 9:
            stairs[i][j] = stairs[i-1][j-1]

for s in stairs:
    print(s)

print(sum(stairs[N-1]) % 1000000000)