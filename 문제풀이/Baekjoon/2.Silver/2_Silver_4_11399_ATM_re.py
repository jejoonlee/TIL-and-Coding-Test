import sys

sys.stdin = open("input.txt")


N = int(input())

array = list(map(int, input().split()))
array.sort()

num = 0
new_array = []

for n in array:
    num += n
    new_array.append(num)

print(sum(new_array))