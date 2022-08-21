import sys
sys.stdin = open('input.txt', 'r')

# 평균과 중앙값 구하기

# 리스트에 넣어서 정렬하기

# 리스트의 총 값과, 길이를 나눠서 평균을 구하고
# 리스트의 길이를 2로 나눠서 나온 값의 인덱스를 중앙값으로 설정한다
# 리스트는 인덱스가 0부터 시작하기 때문에 중앙값을 구할 때 별도로, round를 안 해도 된다

nums = []
for i in range(5):
    num = int(input())
    nums.append(num)

nums.sort()

max_value = sum(nums) / len(nums)

mid_value = int(len(nums) / 2)

print(int(max_value))
print(nums[mid_value])