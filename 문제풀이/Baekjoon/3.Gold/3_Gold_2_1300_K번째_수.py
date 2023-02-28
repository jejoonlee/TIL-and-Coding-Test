import sys
sys.stdin = open('input.txt')

N = int(input())
K = int(input())

left, right = 0, N *N

while left <= right:

    mid = (left + right) // 2
    count = 0

    for num in range(1, N + 1):
        count += min(N, mid // num)

    if count >= K:
        ans = mid
        right = mid - 1

    else:
        left = mid + 1

print(ans)