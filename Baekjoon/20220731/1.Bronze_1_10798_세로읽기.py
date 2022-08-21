# import sys
# sys.stdin = open('input.txt', 'r')

arr = []

for i in range(5):
    input_ = input()
    arr.append(input_)

len_list = []
for leng in arr:
    length = len(leng)
    len_list.append(length)
    max_len = max(len_list)

for i in range(max_len):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')