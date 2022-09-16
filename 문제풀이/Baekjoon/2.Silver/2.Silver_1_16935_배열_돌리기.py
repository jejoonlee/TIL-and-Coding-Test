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

    elif com == 3:
        result = [[0] * N for _ in range(M)]
        for r in range(M):
            for c in range(N):
                result[r][c] = matrix[N - 1 - c][r]
        matrix = result
        M, N = N, M


    elif com == 4:
        result = [[0] * N for _ in range(M)]
        for r in range(M):
            for c in range(N):
                result[r][c] = matrix[c][M - 1 - r]
        matrix = result
        M, N = N, M

    elif com == 5:
        n, m = int(N/2), int(M/2)
        for r in range(N):
            for c in range(M):
                # 4 -> 1
                if r < n and c < m:
                    result[r][c] = matrix[r - n][c]

                # 1 -> 2
                if r < n and m <= c < M:
                    result[r][c] = matrix[r][c - m]

                # 2 -> 3
                if n <= r < N and m <= c < M:
                    result[r][c] = matrix[r - n][c]

                # 3 -> 4
                if n <= r < N and c < m:
                    result[r][c] = matrix[r][c + m]

    elif com == 6:
        n, m = int(N/2), int(M/2)
        for r in range(N):
            for c in range(M):
                # 2 -> 1
                if r < n and c < m:
                    result[r][c] = matrix[r][c + m]

                # 3 -> 2
                if r < n and m <= c < M:
                    result[r][c] = matrix[r + n][c]

                # 4 -> 3
                if n <= r < N and m <= c < M:
                    result[r][c] = matrix[r][c - m]

                # 1 -> 4
                if n <= r < N and c < m:
                    result[r][c] = matrix[r - n][c]

pprint(result)