import sys
input=sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(N)]

r_num = int(input())

for r in range(r_num):
    i, j, x, y = map(int, input().split())
    result = 0
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            result += matrix[a][b]
    print(result)