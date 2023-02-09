import sys
sys.stdin = open('input.txt')

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):          # 경유하는 곳
    for j in range(N):      # 시작점
        for k in range(N):  # 목적지 

            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

print(graph)