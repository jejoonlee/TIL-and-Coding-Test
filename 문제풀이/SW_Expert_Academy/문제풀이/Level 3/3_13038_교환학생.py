import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):

  n = int(input())

  # 숫자 리스트를 2번을 반복한 것으 수업 일 수가 2개 이상일 때에 날에 간격때문에
  # 일수가 바뀔 수 있다
  # [1, 0, 0, 0, 1, 0, 1]
  # 같은 경우 그대로 사용하면 나중에 1, 0, 0, 0, 1 사이에 날 수가 만아진다
  # 그래서 두번째 1, 그리고 세번째 1부터 시작하는 일 수도 따져봐야 한다 
  days = list(map(int, input().split())) * 2

  # 1부터 시작하는 가능한 일 수
  days_p = []

  # 제일 앞의 숫자가 1로 될 수 있도록  만든다
  # 대학교 생활의 최소 일수를 구해야 하는 것이니깐,
  # 수업이 시작하는 날의 기준부터 배열이 시작해야 한다
  for i in range(7):
    if days[i] == 1:

      # 슬라이싱을 통해 1부터 시작할 때의 리스트들을 days_p에 넣는다
      lst = list(days[i : i + 7])
      days_p.append(lst)
  

  # 한 주에 들어야 하는 수업의 양
  lesson = sum(days[0 : 7])

  # # 수업을 들어야하는 주. 몫을 반환
  weeks = n // lesson

  # # 마지막 주에 들어야 하는 수업의 일 수
  day = n % lesson

  result = 0
  if lesson == 1:
    result = ((weeks - 1) * 7) + 1

  else:
    result = weeks * 7
    min_cnt = 0

    for i in range(len(days_p)):
      day_cnt = 0
      cnt = 0
      for j in range(7):

        if days_p[i][j] == 1:
          day_cnt += 1
          cnt += 1

          if cnt == day:
            temp = cnt

            # 최소의 일수를 나타내는 방법
            if temp <= cnt:
              min_cnt = temp
              break

        else:
          day_cnt += 1
    
    result += min_cnt
          
  
  print(f'#{t} {result}')




# 시간 초과
# from collections import deque

# T = int(input())

# for t in range(1, T + 1):

#   n = int(input())

#   days = deque(list(map(int, input().split())))
#   cnt = 0
#   day_count = 0

    # 1이 제일 앞에 올때까지 0을 뒤로 보낸다
#   for day in range(7):
#     if days[0] == 0:
#       days.append(days[0])
#       days.popleft()

      # 순회하면서 1을 발견하면 cnt와 day_count를 세기 시작한다
      # 여기서 cnt는 수업을 듣는 일수
      # day_count는 대학교에 생활하는 일수이다
#     elif days[0] == 1:
#       cnt += 1
#       day_count += 1
      
      # n (들어야 하는 수업의 수) 와 cnt 숫자가 같아질때까지 while문을 돌린다
#       while n != cnt:

          # for 문을 계속 돌면서 day_count는 계속 1씩 누적을 하고
          # 반대로 1, 즉 수업이 있는 날에는 day_count에다 cnt까지 1씩 누적한다
#         for d in range(7):
#           if days[d] == 1:
#             day_count += 1
#             cnt += 1
          
#           else:
#             day_count += 1
#       break
  
#   print(f'#{t} {day_count}')
