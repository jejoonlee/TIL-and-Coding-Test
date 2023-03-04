import sys
from pprint import pprint
sys.stdin = open('input.txt')

N = int(input())
M = int(input())

matrix = [[0] * N for _ in range(N)]

dr = [1, 0 , -1, 0]
dc = [0, 1, 0, -1]

num, i, j = N * N, 0, 0
ans_row, ans_column = 0, 0

while num > 0:

    while i < N and matrix[i][j] == 0:
        if num == M:
            ans_row, ans_column = i + 1, j + 1
        matrix[i][j] = num
        num, i = num - 1, i + 1

        
    i, j = i - 1, j + 1

    while j < N and matrix[i][j] == 0:
        if num == M:
            ans_row, ans_column = i + 1, j + 1
        matrix[i][j] = num
        num, j = num - 1, j + 1

    
    i, j = i - 1 , j - 1

    while i >= 0 and matrix[i][j] == 0:
        if num == M:
            ans_row, ans_column = i + 1, j + 1
        matrix[i][j] = num
        num, i = num - 1, i - 1

    
    i, j = i + 1, j - 1

    while j >= 0 and matrix[i][j] == 0:
        if num == M:
            ans_row, ans_column = i + 1, j + 1
        matrix[i][j] = num
        num, j = num - 1, j - 1


    i, j = i + 1, j + 1

for m in matrix:
    print(' '.join(map(str, m)))
print(ans_row, ans_column)