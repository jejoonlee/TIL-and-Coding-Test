import sys
sys.stdin = open('input.txt')

# 중요한 것은 N kg을 5와 3으로 딱 맞춰야 한다
# 5가 더 큰 수고, 5로 나눠야 봉지 개수가 더 적어지니깐, 먼저 5를 위주로 빼고,
# 그 이후 3으로 채워준다

N = int(input())
cnt = 0
flag=True

while True:
  if N % 5 == 0:
    result = N//5
    cnt += result
    break

  N -= 3
  cnt += 1

  if N < 0 :
    flag=False
    break
  
if flag==True:
  print(cnt)
else:
  print(-1)