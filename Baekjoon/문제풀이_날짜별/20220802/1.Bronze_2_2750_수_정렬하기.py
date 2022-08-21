N = int(input())

nums = []
for n in range(N):
    number = int(input())
    nums.append(number)

nums.sort()

print(*nums, sep = '\n')