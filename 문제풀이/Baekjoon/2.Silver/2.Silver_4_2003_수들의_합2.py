import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

nums = list(map(int, input().split()))
cnt = 0

for i in range(N):

  # M과 같거나, 크면, 0으로 초기화
  add_num = 0
  while True:
    # 리스트를 안에서 while문이 순회할 수 있도록
    if i < N:

      # add_num에 nums 리스트에 있는 숫자를 순차적으로 더함
      add_num += nums[i]

      # M과 add_num이 같으면 cnt에 1을 누적하고, break
      if add_num == M:
        cnt += 1
        break

      # M보다 크면 while문을 바로 break
      elif add_num > M:
        break

      # M보다 작으면 그 다음 인덱스로 이동하기 위해 i에 1을 누적
      else:
        i += 1
    else:
      break

print(cnt)



# 시간 초과
# 슬라이싱을 통해 값들을 더하고, M을 만들 수 있는지 보는 것
# M보다 커지게 되면 for j 문 을 break
# for i in range(N):
#   for j in range(1, N + 1):
#     if sum(nums[i : j]) == M:
#       cnt += 1
#       break

# print(cnt)

# 시간 초과
# for i in range(N):
#   idx = i + 1
#   while True:
#     if idx <= N:
#       num = sum(nums[i:idx])
#       if num == M:
#         cnt += 1
#         break
#       elif num > M:
#         break
#       else:
#         idx += 1
#     else:
#       break

# print(cnt)