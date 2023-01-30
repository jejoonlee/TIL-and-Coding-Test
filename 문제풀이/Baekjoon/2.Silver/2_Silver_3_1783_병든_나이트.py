import sys
sys.stdin = open('input.txt')

import math

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, int(math.ceil(M/2))))
elif M <= 6:
    print(min(4, M))
else:
    print(M-2)