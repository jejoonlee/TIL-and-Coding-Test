
num = int(input())

part = {}

for n in range(num * 2 - 1):
    name = input()
    if name not in part:
        part[name] = 1
    else:
        part[name] += 1

for key, value in part.items():
    if value % 2 == 1:
        print(key)