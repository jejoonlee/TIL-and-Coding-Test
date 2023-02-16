import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start, count):
    visited[start] = count
        
    for cur in graph[start]:
        if visited[cur] == -1:
            dfs(cur, count + 1)
                

N, M, start = map(int, input().split())

visited = [-1] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort(reverse=True)

stack = []

dfs(start, 0)

for i in range(1, len(visited)):
    print(visited[i])