import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

fish = [list(map(int, input())) for _ in range(N)]


for i in range(N):
    print(*fish[i][::-1], sep = '')