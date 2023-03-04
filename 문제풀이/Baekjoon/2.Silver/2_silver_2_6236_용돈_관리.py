import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

spend = [int(input()) for _ in range(N)]

left, right, result = min(spend), sum(spend), 0

while left <= right:
    mid = (left + right) // 2
    daily_spend = mid

    count = 1
    
    for money in spend:
        if daily_spend < money:
            count += 1
            daily_spend = mid
        daily_spend -= money

    print(left, right, mid, count)

    if count > M or max(spend) > mid:
        left = mid + 1

    else:
        right = mid - 1
        result = mid

print(result)