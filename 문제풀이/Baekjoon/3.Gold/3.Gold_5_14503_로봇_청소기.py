import sys
sys.stdin = open('input.txt')

# 지정한 위치에 로봇 배치
# 1. 현재 위치를 청소
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색
    # - 왼쪽에 청소를 안 했으면, 그 방향으로 회전 후 그 칸으로 이동하고 1번으로
    # - 청소할 공간이 없으면, 그 방향으로 회전하고 2번으로 돌아간다
    # - 네 방향 모두 청소가 이미 되어있거나 벽이면, 바라보는 방향을 유지하고 후진하고 2번으로
    # - 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없으면 작동 끝


# 북, 동, 남, 서
# 3,2,1,0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())


land = [list(map(int, input().split())) for _ in range(N)]

# 청소한 칸의 개수
result = 0

while True:
  if land[r][c] == 0:
    land[r][c] = 2
    result += 1

  