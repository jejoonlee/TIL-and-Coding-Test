
import sys
import math

input = sys.stdin.readline

t = int(input())

nums = []
for _ in range(t):
    nums.append(int(input()))

dif = []
for i in range(1, t):
    dif.append(nums[i] - nums[i - 1])

num = math.gcd(dif[0], dif[1])

for i in range(2, len(dif)):
    num = math.gcd(num, dif[i])

answer = 0
for n in dif:
    answer += (n // num) - 1

print(answer)