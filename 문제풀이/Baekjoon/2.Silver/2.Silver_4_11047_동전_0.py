import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

money = [int(input()) for _ in range(N)]
count = 0

while money:
    digit = money.pop()

    if digit <= K:
        count += K // digit
        K %= digit

print(count)