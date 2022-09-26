import sys
sys.stdin = open('input.txt')

# 순회하면서 앞 뒤로 비교를 해서
# 해당 숫자가 앞과 뒤의 중간에 있으면 평범한 숫자

T = int(input())

for t in range(1, T + 1):
  N = int(input())
  nums = list(map(int, input().split()))
  cnt = 0

  for n in range(1, N - 1):
    # 중간 숫자가 앞과 뒤 숫자보다 모두 크거나, 중간 숫자가 앞과 뒤 숫자보다 모두 작으면 
    # cnt에 1을 누적 안 한체 넘어 간다
    if (nums[n] > nums[n - 1] and nums[n] > nums[n + 1]) or (nums[n] < nums[n - 1] and nums[n] < nums[n + 1]):
      continue

    # 반대로 중간 숫자가 앞과 뒤의 숫자의 중간이면, cnt에 1을 누적시킨다
    else:
      cnt += 1
    
  print(f'#{t} {cnt}')
