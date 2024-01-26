
n, k = map(int, input().split(' '))

nums = []

for i in range(1, n + 1):
    if n % i == 0:
        nums.append(i)

if k > len(nums):
    print(0)
else:
    print(nums[k - 1])