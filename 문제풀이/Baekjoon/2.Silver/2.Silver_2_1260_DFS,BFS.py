import sys
sys.stdin = open('input.txt')

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[0] = 'V'

for _ in range(M):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)


stack = [V]
result = []

while len(result) != N:
  current = stack.pop()
  result.append(current)
  
  if visited[current] == 0:
    visited[current] = 'V'
    graph[current].sort(reverse=True)

    for cur in graph[current]:
      if visited[cur] == 0:
        stack.append(cur)

print(result)