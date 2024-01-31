import sys

input = sys.stdin.readline

n = int(input())

atWork = {}

for _ in range(n):
    name, action = map(str, input().split(" "))

    if name not in atWork:
        atWork[name] = "enter"

    elif name in atWork:
        atWork.pop(name)

nameList = sorted(atWork.keys(), reverse=True)

for k in nameList:
    print(k)
