import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

stack = [[] for _ in range(7)]

count = 0
for _ in range(N):
    l, p = map(int, input().split())

    while stack[l] and stack[l][-1] > p:
        stack[l].pop()
        count += 1

    if not stack[l] or stack[l][-1] < p:
        stack[l].append(p)
        count += 1

print(count)
