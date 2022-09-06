
# from pprint import pprint
# import sys
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

chess = [list(input()) for c in range(8)]

piece = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if 'F' == chess[i][j]:
                piece += 1
        else:
            piece += 0


print(piece)