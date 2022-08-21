import sys
sys.stdin = open('input.txt', 'r')

nums = []
for i in range(10):
    num = int(input())
    nums.append(num)

av = sum(nums) / 10

print(int(av))

num_dict = {}
for i in nums:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1

max_value = max(num_dict.values())

most = []
for key, value in num_dict.items():
    if value == max_value:
        most.append(key)

print(max(most))