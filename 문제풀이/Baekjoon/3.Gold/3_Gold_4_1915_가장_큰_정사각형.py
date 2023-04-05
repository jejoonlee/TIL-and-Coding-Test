import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
dp_table = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):

        if matrix[i][j] == 1:
            dp_table[i][j] = 1

            if 0 <= i - 1 and 0 <= j - 1:
                dp_table[i][j] = min(dp_table[i - 1][j], dp_table[i - 1][j - 1], dp_table[i][j - 1]) + 1

result = 0        
for d in dp_table:
    result = max(result, max(d))

print(result ** 2)