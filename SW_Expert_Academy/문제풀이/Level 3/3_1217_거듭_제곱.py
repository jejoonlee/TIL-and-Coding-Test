import sys
sys.stdin = open('input.txt')

def power(n, m):
    if m == 0:
        return 1
    else:       
        return n * power(n, m - 1)


for _ in range(10):
    t = int(input())
    N, M = map(int, input().split())
    result = power(N, M)

    print(f'#{t} {result}')