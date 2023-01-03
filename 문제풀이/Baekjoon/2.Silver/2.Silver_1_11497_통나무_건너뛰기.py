import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    N = int(input())

    array = list(map(int, input().split()))

    array.sort(key=lambda x: x)

    timber = [0] * N
    
    even, odd = 0, -2

    for n in range(N):
        if n % 2 == 0:
            timber[n + even] = array[n]
            even -= 1
        else:
            timber[n + odd] = array[n]
            odd -= 3

    result = abs(timber[0] - timber[-1])

    for i in range(N - 1):
        height_difference = abs(timber[i] - timber[i + 1])
        if height_difference > result:
            result = height_difference

    print(result)