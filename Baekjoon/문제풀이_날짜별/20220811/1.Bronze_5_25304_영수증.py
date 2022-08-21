
import sys
sys.stdin = open('input.txt', 'r')

# 총 금액

total = int(input())

# 물건 종류의 수

N = int(input())

cost = []
for i in range(N):
    # 'a' is price, 'b' is quantity
    a, b = map(int, input().split())
    cost.append(a * b)

real_total = sum(cost)

if real_total == total:
    print('Yes')
else:
    print('No')