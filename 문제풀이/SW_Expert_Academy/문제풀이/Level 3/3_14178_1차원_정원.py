
import sys
sys.stdin = open('input.txt')

import math

T = int(input())

for t in range(1, T + 1):
    N, D = map(int, input().split())

    result = (N / (D * 2 + 1))

    print(f'#{t} {math.ceil(result)}')