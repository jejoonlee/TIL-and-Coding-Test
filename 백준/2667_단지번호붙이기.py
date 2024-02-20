import sys
from collections import deque

dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def bfs(x, y):
    count = 1
    queue = deque()
    queue.append([x, y])
    map[x][y] = 'x'

    while queue:
        current = queue.popleft()

        for i in range(4):
            sr, sc = current[0] + dir[i][0], current[1] + dir[i][1]

            if 0 <= sr < n and 0 <= sc < len(map[0]):
                if map[sr][sc] == '1':
                    map[sr][sc] = 'X'
                    queue.append([sr, sc])
                    count += 1
    
    return count

input = sys.stdin.readline

n = int(input())

map = []

for _ in range(n):
    map.append(list(input().strip()))

aptCount = 0
apt = []

for i in range(n):
    for j in range(len(map[i])):
        if map[i][j] == '1':
            aptCount += 1
            cnt = bfs(i, j)
            apt.append(cnt)

print(aptCount)
apt.sort()
for size in apt: print(size)