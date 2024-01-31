import sys

input = sys.stdin.readline

n = int(input())

num, i, numAdd   = 3, 1, 5

while num < n:
    num += numAdd
    numAdd += 2
    i += 1

print(i)