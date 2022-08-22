
import sys
sys.stdin = open('input.txt')

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

result = {}
for i in range(N):
    result[cards[i]] = 0

for j in range(M):
    if check[j] in result:
        print(1, end = ' ')
    else:
        print(0, end = ' ')