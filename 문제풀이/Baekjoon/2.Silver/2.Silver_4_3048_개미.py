import sys
sys.stdin = open('input.txt')

# group
one, two = map(int, input().split())

first = list(input()) 
second = list(input()) 

T = int(input())

ants = first[::-1] + second 

for t in range(1, T + 1):
  for i in range(len(ants) - 1):

    # 현제 인덱스와 앞에 있는 인덱스를 비교한다
    # 현제 인덱스는 first 리스트에 있어야 하고, 앞의 인덱스는 second 리스트에 있어야 if문이 성립
    if ants[i] in first and ants[i + 1] in second:
      # 성립할 시에, 현제와 앞에 있는 인덱스 값을 바꿔준다
      ants[i], ants[i + 1] = ants[i + 1], ants[i]
      
      # 만약 바꾼 인덱스 값이, first리스트의 제일 첫번째 개미일 때 break
      if ants[i + 1] == first[0]:
        break


print(''.join(ants))