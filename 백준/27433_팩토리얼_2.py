
import sys

input = sys.stdin.readline

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(int(input())))