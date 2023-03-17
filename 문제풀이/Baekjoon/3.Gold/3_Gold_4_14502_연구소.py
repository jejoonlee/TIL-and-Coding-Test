import sys
sys.stdin = open('input.txt')

from collections import deque
from itertools import combinations, permutations
from copy import deepcopy

N, M = map(int, input().split())

virus_map = [list(map(int, input().split())) for _ in range(N)]

def bfs(temp_virus, virus_queue):

    dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]

    virus_count = 2

    while virus_queue:
        r, c = virus_queue.popleft()

        for i in range(4):
            sr, sc = dr[i] + r ,dc[i] + c

            if 0 <= sr < N and 0 <= sc < M:
                if temp_virus[sr][sc] == 0:
                    virus_count += 1
                    temp_virus[sr][sc] = 2
                    virus_queue.append((sr, sc))
    
    return virus_count

queue = deque()
empty_space = []
empty_count = 0
result = N * M

for i in range(N):
    for j in range(M):
        if virus_map[i][j] == 2:
            queue.append((i, j))
        elif virus_map[i][j] == 0:
            empty_space.append((i,j))
            empty_count += 1


for empty in combinations(empty_space, 3):
    temp_map = deepcopy(virus_map)
    virus_queue = deepcopy(queue)

    for e in empty:
        temp_map[e[0]][e[1]] = 1

    result = min(bfs(temp_map, virus_queue), result)

print(empty_count - (result + 1))