import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

names = {}

for _ in range(n):
    names[input().strip()] = 1

answer = []

for _ in range(m):
    name = input().strip()
    if name in names:
        answer.append(name)

print(len(answer))
answer.sort()

for n in answer: print(n)