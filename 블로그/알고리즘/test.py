import sys
sys.stdin = open('input.txt')

from itertools import permutations

small = [int(input()) for _ in range(9)]


for num in permutations(small, 7):
    height = sum(num)

    if height == 100:
        result = [i for i in num]
        result.sort()
        break

for r in result:
    print(r)