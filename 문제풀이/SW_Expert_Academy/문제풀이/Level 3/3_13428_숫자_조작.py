import sys
sys.stdin = open('input.txt')

# 숫자 안에 제일 작은 숫자가 앞에 있으면 그 숫자가 최소값
# 제일 큰 숫자가 앞에 있으면 최댓값
# 하지만 0이 제일 앞에 올 수 없음

T = int(input())

for t in range(1, T + 1):
  num = list(map(int, str(input())))
  length = len(num)
  low = [0] * length
  high = [0] * length

  h, m = max(num), min(num)

  for i in range(length):
    if num[0] == m:
      while i != length:
        low[i] = num[i]
        i += 1
    
    elif num[0] != m and num[i] != m:
      low[i] = num[i]

    elif num[i] == m:
      low[i] = low[0]
      low[0] = m

  for i in range(length):
    if num[0] == h:
      while i != length:
        high[i] = num[i]
        i += 1

    elif num[0] != h and num[i] != h:
      high[i] = num[i]

    elif num[i] == h:
      high[i] = high[0]
      high[0] = h

  print(low, high)