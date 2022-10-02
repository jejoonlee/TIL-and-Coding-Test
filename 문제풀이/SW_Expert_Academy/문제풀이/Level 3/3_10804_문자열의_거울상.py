import sys
sys.stdin = open('input.txt')

T = int(input())

mirror = {'d': 'b', 'b' : 'd', 'p' : 'q', 'q' : 'p'}

for t in range(1, T + 1):
  words = input()

  result = []

  for i in words[::-1]:
    result.append(mirror[i])

  result = ''.join(result)
  print(f'#{t} {result}')