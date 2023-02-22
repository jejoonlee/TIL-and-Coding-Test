import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open('input.txt')


def dfs(start, weight):

    for node, wei in tree[start]:
        if visited[node] == -1:
            visited[node] = weight + wei
            dfs(node, weight + wei)
    
            
n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
visited[1] = 0

for _ in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

dfs(1, 0)

second_index = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[second_index] = 0
dfs(second_index, 0)

print(max(visited))