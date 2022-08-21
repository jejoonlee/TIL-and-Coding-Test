# https://www.acmicpc.net/problem/2908
from math import remainder
from re import I
import sys

sys.stdin = open("1_상수.txt")

# a, b = map(int, input().split())

# reverse_num_a = 0

# while a:
#     leftover = a % 10
#     reverse_num_a = reverse_num_a * 10 + leftover
#     a = a // 10
# # a의 10으로 나눈 나머지를
# # 일의 숫자에 더한다
# # a와 10의 나눈 몫을 가지고 오면, a의 자릿수는 하나 줄어든다

# # 줄어든 a를 다시 10으로 나누고
# # 전에 숫자를 10으로 곱하고, 새로운 a의 나머지를 더한다
# # 그리고 a의 나눈 몫을 가지고 오면 또 a 자릿수는 하나 줄어들고
# # 이후 계속 반복하면 숫자가 거꾸로 되어 있다


# reverse_num_b = 0

# while b:
#     leftover = b % 10
#     reverse_num_b = reverse_num_b * 10 + leftover
#     b = b // 10

# if reverse_num_a > reverse_num_b:
#     print(reverse_num_a)
# else:
#     print(reverse_num_b)

a, b = input().split()

reverse_a = int(a[::-1])
reverse_b = int(b[::-1])

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)
