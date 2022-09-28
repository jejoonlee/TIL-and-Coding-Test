import sys
sys.stdin = open('input.txt')

# 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 판정

# 'o'를 만나면 8면을 탐색을 한다
# 8면을 탐색 후, 만약 'o'가 존재하면, 그 방향으로 '.' 또는 리스트 밖으로 나갈때까지 탐색한다
# cnt가 5개면 바로 YES를 출력하고 끝낸다

T = int(input())

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for t in range(1, T + 1):
  N = int(input())
  board = [list(input()) for _ in range(N)]
  flag = False

  for r in range(N):
    if flag == True:
      break
    
    for c in range(N):
      if board[r][c] == 'o':

        for i in range(8):
          sr = dr[i] + r
          sc = dc[i] + c
          cnt = 1

          if flag == True:
            break

          while True:
            if 0 <= sr < N and 0 <= sc < N:
              if board[sr][sc] == 'o':
                cnt += 1
                sr += dr[i]
                sc += dc[i]
                if cnt == 5:
                  flag = True
                  break
              else:
                break
            else:
              break

  if flag == True:
    print(f'#{t} YES')
  else:
    print(f'#{t} NO')