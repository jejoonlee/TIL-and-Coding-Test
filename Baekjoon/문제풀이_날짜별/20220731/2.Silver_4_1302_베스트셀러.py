import sys
sys.stdin = open('input.txt', 'r')

sell = int(input())

books = {}
name_list = []

for i in range(sell):
    names = input()
    name_list.append(names)

for name in name_list:
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

max_num = max(books.values())

best = []
for key, value in books.items():
    if value == max_num:
       best.append(key)

best.sort()

print(best[0]) 