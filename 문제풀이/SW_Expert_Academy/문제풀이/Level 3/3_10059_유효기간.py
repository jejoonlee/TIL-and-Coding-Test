import sys
sys.stdin = open('input.txt')

T = int(input())

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for t in range(1, T + 1):
  N = input()

  if N[0:2] in month and N[2:4] not in month:
    print(f'#{t} MMYY')
  elif N[0:2] not in month and N[2:4] in month:
    print(f'#{t} YYMM')
  elif N[0:2] not in month and N[2:4] not in month:
    print(f'#{t} NA')
  elif N[0:2] in month and N[2:4] in month:
    print(f'#{t} AMBIGUOUS')