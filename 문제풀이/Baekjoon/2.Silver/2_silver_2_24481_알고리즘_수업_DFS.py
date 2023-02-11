import sys

sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

def dfs(start, count):
    result[start] = count

    for num in tree[start]:
        if result[num] == -1:
            dfs(num, count + 1)

n, m, r = map(int, input().split())

tree = [[] for _ in range(n + 1)]
result = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for t in tree:
    t.sort()

dfs(r, 0)

for i in range(1, n+1):
    print(result[i])