import sys
sys.stdin = open('input.txt', 'r')

arrs = int(input())

for a in range(arrs):
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    print(arr[2])