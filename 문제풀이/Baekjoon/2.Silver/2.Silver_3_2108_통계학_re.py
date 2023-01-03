import sys
sys.stdin = open("input.txt")

N = int(input())

array = []

for _ in range(N):
    array.append(int(input()))

array.sort(key=lambda x: x)


# 모든 수들의 합
total = 0
for num in array:
    total += num

average = total / N

print(round(average))

# 중앙 값
print(array[N//2])

# 최빈값
most_num = {}
for num in array:
    if num in most_num:
        most_num[num] += 1
    else:
        most_num[num] = 1

most_value = max(most_num.values())

most_nums = []
for key, value in most_num.items():
    if value == most_value:
        most_nums.append(key)

if len(most_nums) == 1:
    print(most_nums[0])
else:
    print(most_nums[1])


#최댓값과 최소값의 차이
print(array[-1] - array[0])