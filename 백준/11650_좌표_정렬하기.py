
import sys

nums = []

for _ in range(int(sys.stdin.readline())):
    nums.append(list(map(int, sys.stdin.readline().split(' '))))

nums.sort(key = lambda x : (x[0], x[1]))

for num in nums:
    print(num[0], num[1])