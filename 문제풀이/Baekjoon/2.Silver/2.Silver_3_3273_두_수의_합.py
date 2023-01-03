import sys

sys.stdin = open("input.txt")

n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort(key=lambda x: x)

cnt = 0
i = 0
j = n - 1

while i != j:

    if array[i] + array[j] == x:
        cnt += 1
        i += 1

    elif array[i] + array[j] > x:
        j -= 1

    elif array[i] + array[j] < x:
        i += 1

print(cnt)
