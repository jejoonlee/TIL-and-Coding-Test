n, k = map(int, input().split(" "))
nums = sorted(list(map(int, input().split(" "))), reverse=True)

print(nums[k - 1])
