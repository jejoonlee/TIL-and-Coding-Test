import sys
sys.stdin = open('input.txt')

def pprint(lst):
    for i in lst:
        print(i)

N, M, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*M for _ in range(N)]

command = list(map(int, input().split()))

for com in command:
    
    if com == 1:
        for r in range(N):
            for c in range(M):
                result[r][c] = matrix[N - 1 - r][c]
        matrix = result

    elif com == 2:
        for r in range(N):
            for c in range(M):
                result[r][c] = matrix[r][M - 1 - c]
        matrix = result


pprint(result)