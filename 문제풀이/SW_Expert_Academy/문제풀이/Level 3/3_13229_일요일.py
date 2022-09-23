import sys
sys.stdin = open('input.txt')

# 다음 일요일까지 남은 일 수
# 지금 일요일이라면 일주일 후 일요일과 남은 일 수를 구한다
# 일주일에 7일이 있고, 'S'라는 리스트에 일요일부터 넣어서
# 7을 주어진 날의 'S' 리스트에 있는 인덱스를 뺀다

T = int(input())

S = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for t in range(1, T + 1):
  day = input()

  print(f'#{t} {7 - S.index(day)}')