import sys
sys.stdin = open('input.txt')

Num = int(input())

cache = [0] * 1001
cache[1], cache[2] = 1, 2

for i in range(3, 1001):
    cache[i] = cache[i - 1] + cache[i - 2]


print(cache[Num] % 10007)

# 1 2 3 4 5 6  7  8  9
# 1 2 3 5 8 13 21 34 55