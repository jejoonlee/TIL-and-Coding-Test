import sys
sys.stdin = open('input.txt')

# 재귀함수 사용

for t in range(int(input())):
    n, r = map(int, input().split())

    # factorial = N * (N - 1)!
    def factorial(N):
        if N <= 1:
            return 1
        else:
            return N * factorial(N - 1)

    # combination = n! / r! (n - r)!

    combination = factorial(n) / (factorial(r) * factorial(n - r))

    print(f'#{t + 1} {int(combination)}')



# def factorial(x):
#     result = 1
#     for i in range(1, x +1):
#         result *= i
#     return result


# for t in range(int(input())):
#     N, R = map(int, input().split())


#     print(f'#{t + 1} {int(final)}')

# for t in range(int(input())):
#     N, R = map(int, input().split())

#     num_1 = 1
#     for i in range(R + 1, N + 1):
#         num_1 *= i

#     num_2 = 1
#     for j in range(1, (N - R) + 1):
#         num_2 *= j

#     print(f'#{t + 1} {int(num_1 / num_2)}')