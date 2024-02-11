from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split(' '))

queue = deque()
nodes, visited = [[] for _ in range(n + 1)], [0] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split(' '))
    nodes[s].append(e)
    nodes[e].append(s)

queue.append(r)
visited[r], count = 1, 1

while queue:
    current = queue.popleft()

    nodes[current].sort(key=lambda x : -x)

    for node in nodes[current]:
        if visited[node] == 0:
            count += 1
            visited[node] = count
            queue.append(node)

for i in range(1, n + 1): print(visited[i])
