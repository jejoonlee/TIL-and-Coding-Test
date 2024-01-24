
nums = list(map(int, input().split(' ')))

A, B, C = nums[0], nums[1], nums[2]

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)