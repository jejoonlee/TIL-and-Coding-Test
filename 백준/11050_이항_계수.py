
import sys, math

input = sys.stdin.readline

n, k = map(int, input().split(' '))

print(int(math.factorial(n)) // (int(math.factorial(k)) * (int(math.factorial(n - k)))))