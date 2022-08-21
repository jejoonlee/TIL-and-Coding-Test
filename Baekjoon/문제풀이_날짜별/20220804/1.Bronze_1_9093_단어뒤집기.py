import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

for n in range(N):
    sen = list(input().split())
    for s in sen:
        print(s[::-1], end = ' ',)
    print('')