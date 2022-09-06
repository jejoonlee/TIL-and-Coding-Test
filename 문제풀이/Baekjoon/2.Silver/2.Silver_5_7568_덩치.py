import sys

sys.stdin = open('input.txt', 'r')

# 키와 몸무게가 모두 커야 덩치가 더 큰 것
# 자신보다 더 덩치가 큰 사람들이 있으면 k + 1

N = int(input())

lst = []
for i in range(1, N + 1):
    x, y = map(int, input().split())
    lst.append((x, y))

rank = [0] * N

for a in range(N):
    A = lst[a]
    for b in range(N):
        B = lst[b]
        if A[0] > B[0] and A[1] > B[1]:
            rank[b] += 1

for result in rank:
    print(result + 1, end = ' ')