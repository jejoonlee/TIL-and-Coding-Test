import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

check = {}
for i in range(N):
    check[input()] = 0

cnt = 0
for j in range(M):
    word = input()
    if word in check:
        cnt += 1

print(cnt)