import sys
sys.stdin = open('input.txt', 'r')


colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

c_lst = []
for i in range(3):
    c = input()
    c_lst.append(c)

for i in range(len(colors)):
    if colors[i] == c_lst[0]:
        res_1 = i * 10
    if colors[i] == c_lst[1]:
        res_2 = i
    if colors[i] == c_lst[2]:
        res_3 = 10 ** i

result = (res_1 + res_2) * res_3

print(result)