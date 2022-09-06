import sys
sys.stdin = open('input.txt')

N = int(input())

compare = []
for n in range(N):
    x, y = map(int, input().split())
    compare.append([x, y])

first_sort = sorted(compare)

for i in first_sort:
    print(*i)