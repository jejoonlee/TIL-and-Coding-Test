import sys
sys.stdin = open("input.txt")
from collections import deque

n = int(input())
start, end = map(int, input().split())
start, end = start - 1, end - 1
m = int(input())

relations = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    x, y = map(int, input().split())
    relations[x-1].append((y-1, 0))
    relations[y-1].append((x-1, 0))

visited[start] = True
queue = deque([(start, 0)])


while queue:
    current, count = queue.popleft()

    if current == end:
        break

    for cur in relations[current]:
        if visited[cur[0]] == False:
            visited[cur[0]] = True
            queue.append((cur[0], count + 1))

if visited[end] == True:
    print(count)
else:
    print(-1)