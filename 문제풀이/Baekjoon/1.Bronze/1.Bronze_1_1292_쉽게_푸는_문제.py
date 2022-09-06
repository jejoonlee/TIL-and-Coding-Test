
# 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.
# 이 문제는 다음과 같다. 
# 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

# a, b = map(int, input().split())


# nums =[]
# for i in range(1, b + 1):
#     for j in range(i):
#     # j는 횟수, i는 크기
#         nums.append(i)

# result = sum(nums[a - 1 : b])
    
# print(result)


a, b = map(int, input().split())

n = 1
nums = []

# nums에 얼마만큼 숫자를 추가해야하나?
# nums의 길이가 b보다 작을 떄까지 수열에 숫자를 추가한다
while len(nums) < b:
    #n의 크기만큼 수열 리스트에 n을 추가한다
    for i in range(n):
        nums.append(n)
    n += 1

print(nums)