import sys
sys.stdin = open("input.txt")

numbers = input()

# zero = 0
# one = 0

# if len(numbers) > 1:
#     for i in range(1, len(numbers)):
#         if numbers[i] != numbers[i-1]:
#             if numbers[i-1] == '0':
#                 zero += 1
#             else:
#                 one += 1

# if zero == 0 and one == 0:
#     print(0)
# elif zero == 0:
#     print(one)
# elif one == 0:
#     print(zero)
# else:
#     print(min(one,zero))


count = 0

for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i+1]:
        count += 1

print((count + 1) // 2)