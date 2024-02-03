import sys

input = sys.stdin.readline

n = int(input())
count = 0
gomgom = {}

for _ in range(n):
    
    n = input().strip()

    if n == 'ENTER':
        gomgom = dict()

    else:
        if n not in gomgom:
            gomgom[n] = True
            count += 1

print(count)