
nums, numsAdd = [], 0
for _ in range(5):
    number = int(input())
    numsAdd += number
    nums.append(number)

nums.sort()

print(numsAdd // 5)
print(nums[2])