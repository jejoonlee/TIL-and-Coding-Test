import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
block = list(map(int, input().split()))


water = 0
for i in range(1, M - 1):
    # 해당 자리 양 옆으로, 물이 고일 수 있도록 벽돌이 있는지 확인 하는 것
    left, right = block[:i], block[i + 1:]
    wall = min(max(left), max(right))

    # 고인 물 계산하기
    if wall > block[i]:
        water += wall - block[i]

print(water)