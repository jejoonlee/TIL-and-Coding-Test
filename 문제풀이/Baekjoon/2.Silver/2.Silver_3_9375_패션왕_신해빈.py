import sys
sys.stdin = open('input.txt')

T = int(input())


for _ in range(T):
  N = int(input())
  clothes = []
  for n in range(N):
    A, B = input().split()
    clothes.append((A,B))

  

  print(clothes)