import sys
sys.stdin = open('input.txt')

N = int(input())
array = list(map(int, input().split()))
swap = int(input())

for i in range(N):
    max_num = max(array[i : i + swap + 1])
    max_num_index = array.index(max_num)

    for j in range(max_num_index, i, -1):
        array[j - 1], array[j] = array[j], array[j - 1]

    swap -= max_num_index - i

    if swap <= 0:
        break


print(' '.join(map(str, array)))