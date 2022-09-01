import sys
sys.stdin = open('input.txt')

# 오큰수는 숫자 A에서 오른쪽에 있으면서 A보다 큰 수 중에 가장 왼쪽에 있는 수
# 즉, A와 오른쪽 숫자들을 비교면서, A보다 큰 수 중 제일 먼저 나오는 숫자가 오큰수
# 오큰수가 없을 경우 -1을 출력

# 예) A = [3, 5, 2, 7]
# 3에서 오른쪽 숫자 중 3보다 큰 숫자는 5와 7 / 그중 3과 제일 가까운 수는 5 (오큰수)
# 5랑 오른쪽 숫자들을 비교하면 큰 숫자가 7밖에 없음 오큰수 = 7
# 2 보다 큰 숫자는 7밖에 없음 오큰수 = 7
# 7 오른쪽엔 숫자가 없음 오큰수 = -1

# 5 4 4 5 6 7 8 1 1 8 

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))



#시간 초과
# N = int(input())
# nums = list(map(int, sys.stdin.readline().split()))

# result = []
# for i in range(N):
#     ns = i + 1
#     while True:
#         if ns < N:
#             if nums[i] < nums[ns]:
#                 result.append(nums[ns])
#                 break
#             else:
#                 ns += 1
#         else:
#             result.append(-1)
#             break

# print(*result)