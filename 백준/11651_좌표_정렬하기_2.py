
import sys

array = []
for _ in range(int(sys.stdin.readline())):
    array.append(list(map(int, sys.stdin.readline().split(' '))))

array.sort(key = lambda x : (x[1], x[0]))

for num in array: print(num[0], num[1])