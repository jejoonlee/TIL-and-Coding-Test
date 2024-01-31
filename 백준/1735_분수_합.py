import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))

top = (a * d) + (c * b)
bottom = b * d

divNum = math.gcd(top, bottom)

print(top // divNum, bottom // divNum)