import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos = []
for m in range(M):
    qty = int(input())
    b_num = list(map(int, input().split()))
    for i in range(len(b_num) - 1):
        if b_num[i] > b_num[i + 1]:
            pos.append(1)
        else:
            pos.append(0)

if 0 in pos:
    print('No')
else:
    print('Yes')