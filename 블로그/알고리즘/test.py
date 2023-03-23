import sys
sys.stdin = open('input.txt')

MOD = 10007
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())

cache = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    cache[i][0], cache[i][i] = 1, 1
    
    for j in range(1, i):
        cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]

print(cache[N][K])