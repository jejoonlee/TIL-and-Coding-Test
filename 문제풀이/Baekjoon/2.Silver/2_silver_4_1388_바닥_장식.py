import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

floor = [input() for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M-1):
        if floor[i][j] == "-" and floor[i][j + 1] == "|":
            count += 1
    if floor[i][-1] == "-":
        count += 1

for j in range(M):
    for i in range(N-1):
        if floor[i][j] == "|" and floor[i + 1][j] == "-":
            count += 1
    if floor[N-1][j] == "|":
        count += 1
        
print(count)