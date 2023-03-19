import sys
sys.stdin = open('input.txt')

from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

one = [[-1, 0], [0, -1], [0, 1], [1, 0]] # 1번 CCTV
two = [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]] # 2번 CCTV
three = [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]] # 3번 CCTV
four = [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]] # 4번 CCTV
five = [[(-1, 0), (0, -1), (0, 1), (1, 0)]] # 5번 CCTV

CCTV = []
direction = []

for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            CCTV.append((i, j))
            direction.append(office[i][j]) 