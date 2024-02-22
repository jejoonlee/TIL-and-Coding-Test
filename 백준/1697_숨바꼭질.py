import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split(' '))

visited = [-1] * 100001
visited[n] = 0

def bfs(start):

    global visited

    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()

        nextBack = current - 1
        nextFront = current + 1
        teleport = current * 2

        if nextBack >= 0 and (visited[nextBack] == -1 or visited[current] + 1 < visited[nextBack]):
            queue.append(nextBack)
            visited[nextBack] = visited[current] + 1 
        
        if nextFront < 100001 and (visited[nextFront] == -1 or visited[current] + 1 < visited[nextFront]):
            queue.append(nextFront)
            visited[nextFront] = visited[current] + 1

        if teleport < 100001 and (visited[teleport] == -1 or visited[current] + 1 < visited[teleport]):
            queue.append(teleport)
            visited[teleport] = visited[current] + 1
            
bfs(n)

print(visited[k])