import sys
sys.stdin = open('input.txt')

# 'o' 이면 소정이가 승리 , 'x'면 패했다는 것
# 15번 경기를 진행
# 소정이가 점심값을 면제받기 위해서는 최소 8번을 이겨야 함

T = int(input())

for t in range(1, T + 1):
  armwrestle = input()

  # 이미 팔씨름을 한 갯수
  already = len(armwrestle)
  cnt = 0

  for arm in armwrestle:
    if arm == 'o':
      cnt += 1

  result = (15 - already) + cnt

  if result >= 8:
    print(f'#{t} YES')
  else:
    print(f'#{t} NO')