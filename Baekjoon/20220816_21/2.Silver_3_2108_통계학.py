import sys
sys.stdin = open('input.txt')

# N은 홀수
# 인덱스는 0으로 시작

# N개의 수들의 합을 N으로 나눈 값 / 평균
# N개의 수들의 중앙 값
# N개의 수들 중 가장 많이 나타나는 값
# N개의 수들 중 최댓값과 최솟값의차이

N = int(input())

nums = []
for n in range(N):
    num = int(input())
    nums.append(num)

# 평균
print(round(sum(nums)/N)) 

nums.sort()

# 중앙값 구하기
center = N // 2
print(nums[center]) 

# 최빈값 / 다수면 두번째
diction = {}
for n in nums:
    if n not in diction:
        diction[n] = 1
    else:
        diction[n] += 1

most_value = max(diction.values())

result = []
for i in diction:
    if diction[i] == most_value:
        result.append(i)

if len(result) == 1:
    print(result[0])
else:
    print(result[1])


# 최댓값과 최솟값의 차이
print(nums[-1] - nums[0]) 