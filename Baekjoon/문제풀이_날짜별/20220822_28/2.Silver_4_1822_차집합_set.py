import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a - b
result = list(result)
result.sort()

if len(result) != 0:
    print(len(result))
    print(*result)
else:
    print(0)