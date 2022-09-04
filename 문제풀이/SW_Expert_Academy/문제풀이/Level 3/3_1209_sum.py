import sys
sys.stdin = open('input.txt')

# 각 행의 합, 열, 대각선 중의 합 중 최대값

# 00 01 02 03 0-1 
# 10 11 12 1-2 14 
# 20 21 2-3 23 24 
# 30 3-4 32 33 34 
# 4-5 41 42 43 44 

for _ in range(1, 11):

    t = int(input())

    matrix = [list(map(int, input().split())) for _ in range(100)]

    max_h = 0
    max_v = 0

    for r in range(100):
        horizontal = 0
        vertical = 0
        for c in range(100):
            horizontal += matrix[r][c]
            vertical += matrix[c][r]
        
        if horizontal > max_h:
            max_h = horizontal
        if vertical > max_v:
            max_v = vertical

    # 대각선은 값이 한 개가 나온다
    # 대각선의 인덱스는 row와 column이 같다
    # 반대의 대각선은 row는 그대로 쓰고, 음수를 사용한다
    # 음수는 -1 부터 시작해서, -1을 뺀다
    # 음수를 사용한다는 것은, 리스트를 반대로 순회한다는 것!!!
    cross = 0
    rev_cross = 0
    for d in range(100):
        cross += matrix[d][d]
        rev_cross += matrix[d][-d - 1]

    print(f'#{t} {max(max_h, max_v, cross, rev_cross)}')