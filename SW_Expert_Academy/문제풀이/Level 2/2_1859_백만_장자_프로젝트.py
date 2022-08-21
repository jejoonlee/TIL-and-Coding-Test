import sys
sys.stdin = open('input.txt', 'r')

# 뒤에서부터 계산을 한다
# 맨 뒤에 수를 제일 큰 값으로 지정


T = int(input())

for t in range(1, T + 1):
    n = int(input())
    cost = list(map(int, input().split()))

    revenue = 0
    max_cost = cost[-1]

    for i in range(n)[::-1]:
        if cost[i] >= max_cost:
            max_cost = cost[i]

        # max_cost보다 작다면, 이익을 더해준다
        if cost[i] < max_cost:
            revenue += (max_cost -  cost[i])

    print(f'#{t} {revenue}')