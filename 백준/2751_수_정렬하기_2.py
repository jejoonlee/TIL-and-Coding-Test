import sys

input = sys.stdin.readline

array = []
for _ in range(int(input())):
    array.append(int(input()))

for i in sorted(array):
    print(i)
