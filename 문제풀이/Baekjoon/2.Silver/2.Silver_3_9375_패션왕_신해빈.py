import sys
sys.stdin = open('input.txt')

# 수학
# (종류 + 1) * (종류 + 1)..... -1 
# -1 은 아무것도 착용을 안 했을 때에
# +1 은 해당 종류를 입어도 되고, 안 입어도 되니깐

T = int(input())

for _ in range(T):
  N = int(input())
  clothes = {}
  for n in range(N):
    A, B = input().split()
    
    if B in clothes:
      clothes[B] += 1
    
    elif B not in clothes:
      clothes[B] = 1
      
  result = 1

  for cloth in clothes:
    result *= (clothes[cloth] + 1)

  print(result - 1)