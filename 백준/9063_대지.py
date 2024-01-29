

n = int(input())

xList, yList = [], []

for _ in range(n):
    x, y = map(int, input().split(' '))

    xList.append(x)
    yList.append(y)

if n <= 1:
    print(0)

else:
    print((max(xList) - min(xList)) * (max(yList) - min(yList)))
