import sys

input = sys.stdin.readline

inputString = input().strip()

groupByMinus = list(inputString.split("-"))

if groupByMinus[0] == '':
    groupByMinus.pop(0)

allSums = []

for equation in groupByMinus:
    groupPlus = list(map(int, equation.split("+")))
    allSums.append(sum(groupPlus))

num = allSums[0]

if inputString[0] == '-': num *= -1

for i in range(1, len(allSums)):
    num -= allSums[i]

print(num)
