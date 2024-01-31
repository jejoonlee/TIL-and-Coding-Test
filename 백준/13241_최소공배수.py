import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split(' '))

print(math.lcm(a, b))