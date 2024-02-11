import sys, copy
from collections import deque


def dfs(start):

    global dfsVisited, dfsAnswer

    dfsVisited[start] = 1

    dfsAnswer.append(start)

    dfsNode[start].sort()

    for node in dfsNode[start]:
        if dfsVisited[node] == 0:
            dfs(node)

def bfs(start):
    queue = deque()
    queue.append(start)
    bfsVisited[start] = 1

    while queue:
        current = queue.popleft()
        bfsAnswer.append(current)
        bfsNode[current].sort()

        for node in bfsNode[current]:
            if bfsVisited[node] == 0:
                bfsVisited[node] = 1
                queue.append(node)



input = sys.stdin.readline
n, m, v = map(int, input().split(' '))

dfsNode, dfsVisited, dfsAnswer = [[] for _ in range(n + 1)], [0] * (n + 1), []

for _ in range(m):
    s, e = map(int, input().split(' '))
    dfsNode[s].append(e)
    dfsNode[e].append(s)

bfsNode, bfsVisited, bfsAnswer = copy.deepcopy(dfsNode), [0] * (n + 1), []

dfs(v), bfs(v)

print(' '.join(list(map(str, dfsAnswer))))
print(' '.join(list(map(str, bfsAnswer))))

