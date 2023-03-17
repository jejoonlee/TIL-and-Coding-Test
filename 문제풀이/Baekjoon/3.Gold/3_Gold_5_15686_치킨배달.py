
import sys
sys.stdin = open('input.txt')

from itertools import combinations

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

chicken, home = [], []
result = N ** N

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

        elif city[i][j] == 1:
            home.append((i, j))


for alive in combinations(chicken, M):
    distance = 0
    print(alive)
    print(home)

    for h in home:
        min_distance = N * N
    
        for a in alive:
            dis = abs(h[0] - a[0]) + abs(h[1] - a[1])

            if dis < min_distance:
                min_distance = dis
        
        distance += min_distance

    result = min(distance, result)

print(result)