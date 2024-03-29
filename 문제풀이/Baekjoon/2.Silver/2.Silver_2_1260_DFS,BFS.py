import sys
sys.stdin = open('input.txt')

from collections import deque

DFS_LIST = []
BFS_LIST = []

def dfs(V):
  dfs_visited[V] = 'V'
  DFS_LIST.append(V + 1)

  for i in graph[V]:
    if dfs_visited[i] != 'V':
      dfs(i)

  return DFS_LIST

def bfs(V):
  bfs_visited[V] = 'V'
  queue = deque([V])

  while queue:
    current = queue.popleft()
    BFS_LIST.append(current + 1)

    for cur in graph[current]:
      if bfs_visited[cur] != 'V':
        bfs_visited[cur] = 'V'
        queue.append(cur)

  return BFS_LIST



# N 정점의 개수 / M 간선의 개수 / V 탐색 시작
N, M, V = map(int, input().split())
V = V - 1
graph = [[] for _ in range(N)]
dfs_visited = [0] * (N)
bfs_visited = [0] * (N)

for _ in range(M):
  a, b = map(int, input().split())

  graph[a - 1].append(b - 1)
  graph[b - 1].append(a - 1)

for j in graph:
  j.sort()

print(graph)
print(' '.join(map(str, dfs(V))))
print(' '.join(map(str, bfs(V))))