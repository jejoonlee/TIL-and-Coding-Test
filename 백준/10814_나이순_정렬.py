import sys

array = []
for _ in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().split(" ")
    array.append([int(age), name])

array.sort(key=lambda x: (x[0]))

for info in array:
    print(info[0], info[1][: len(info[1]) - 1])
