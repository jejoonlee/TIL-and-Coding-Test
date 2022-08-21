import sys
sys.stdin = open('input.txt')

# 시간 초과...

# N = int(input())

# lst = list(map(int, input().split()))
# result = [0] * N

# # 중복 값들을 없앤다
# nums = set(lst)
# nums = list(nums)

# # 이중 리스트를 통해 중복 값을 없앤 값들과, 입력 값들을 비교한다
# for i in range(N):
#     for j in range(len(nums)):
#         if lst[i] > nums[j]:
#             result[i] += 1

# print(*result)


N = int(input())

nums = list(map(int, input().split()))
# 중복 값을 없앤다
nums_ord = list(set(nums))
# 중복 값을 없엔 리스트를 오름차순으로 정렬한다
# 그러면 지금 리스트의 인덱스를 통해 앞에 몇 개의 값들이 있는지 확인 가능하다
# 예) [-10, -9, 2, 4]
# 여기서 인덱스를 보면, 0, 1, 2, 3
# -10 앞에 값은 없음 0
# -9 앞에 값이 있어 1 등등...
nums_ord.sort()

nums_dict = {}

for i in range(len(nums_ord)):
    nums_dict[nums_ord[i]] = i

# 만든 딕셔너리에서 값들을 가지고 온다
# nums의 인덱스를 순회하는데, 해당 값을 딕셔너리 key로 설정해서 value를 가지고 온다
for id in nums:
    print(nums_dict[id], end = ' ')
