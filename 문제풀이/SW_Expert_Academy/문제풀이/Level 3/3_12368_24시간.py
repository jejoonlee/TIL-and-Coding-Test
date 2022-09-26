import sys
sys.stdin = open('input.txt')

# 자정부터 A 시간이 지났고
# 추가로 B 시간이 지나면 몇시인가?

# A와 B를 더하고 24로 빼기

T = int(input())

for t in range(1, T + 1):
  A, B = map(int, input().split())
  result = A + B

  if result < 24 :
    print(f'#{t} {result}')
  
  else:
    print(f'#{t} {result - 24}')
