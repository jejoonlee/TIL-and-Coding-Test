
import sys
sys.stdin = open('input.txt')

N = int(input())

arr = []
for n in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
    
arr.sort(key = lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])