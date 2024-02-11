import sys 
input = sys.stdin.readline

sys.setrecursionlimit(150000)

n, m, r = map(int, input().split(' '))

nodes, visited = [[] for _ in range(n + 1)], [0] * (n + 1)

count = 1

for _ in range(m):
    a, b = map(int, input().split(' '))
    nodes[a].append(b)
    nodes[b].append(a)

def dfs(start):
    global visited, count

    sortedNode = sorted(nodes[start])

    for node in sortedNode:
        if visited[node] == 0:
            count += 1
            visited[node] = count
            dfs(node)

visited[r] = 1
dfs(r)

for num in range(1, n + 1): print(visited[num])