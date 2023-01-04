import sys
sys.stdin = open("input.txt")

N = int(input())
array = list(map(int, input().split()))

array.sort(key=lambda x: x)
result = 0

for i in range(N):
    temp = array[:i] + array[i+1:]
    start, end = 0, len(temp) - 1

    while start != end:
        add_num = temp[start] + temp[end]

        if add_num == array[i]:
            result += 1
            break
        elif add_num > array[i]:
            end -= 1
        else:
            start += 1

print(result)