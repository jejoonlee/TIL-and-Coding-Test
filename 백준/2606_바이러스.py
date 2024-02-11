import sys
from collections import deque

input = sys.stdin.readline

com, link = int(input()), int(input())

nodes, visited = [[] for _ in range(com + 1)], [0] * (com + 1)

for _ in range(link):
    com1, com2 = map(int, input().split(" "))

    nodes[com1].append(com2)
    nodes[com2].append(com1)


queue, count = deque(), 0
queue.append(1)
visited[1] = 1

while queue:
    current = queue.popleft()

    for node in nodes[current]:
        if visited[node] == 0:
            visited[node] = 1
            count += 1
            queue.append(node)

print(count)
