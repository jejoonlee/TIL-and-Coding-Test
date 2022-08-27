import sys
sys.stdin = open('input.txt')

# def factorial(x):
#     result = 1
#     for i in range(1, x +1):
#         result *= i
#     return result


# for t in range(int(input())):
#     N, R = map(int, input().split())


#     print(f'#{t + 1} {int(final)}')

for t in range(int(input())):
    N, R = map(int, input().split())

    num_1 = 1
    for i in range(R + 1, N + 1):
        num_1 *= i

    num_2 = 1
    for j in range(1, (N - R) + 1):
        num_2 *= j

    print(f'#{t + 1} {int(num_1 / num_2)}')