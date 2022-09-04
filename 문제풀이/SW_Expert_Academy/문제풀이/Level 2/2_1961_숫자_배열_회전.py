
import sys
sys.stdin = open('input.txt')

# 1. 입력 행열과 결과 행열을 만든다
#    결과 행열은 row N개 / column 3개

# 2. 90도씩 돌아갈때마다 넣을 수 있는 행열을 만든다 (모두 0으로)

T = int(input())

for t in range(1, T + 1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 90도 돌때마다 여기에 저장이 된다
    rotate_90 = [[0] * N for _ in range(N)]

    # 마지막 결과 값을 가져온다
    # column이 3개인 이유는 90도 180도 270도 씩 column이 나눠져 있다
    result = [[0] * 3 for _ in range(N)]

    # 3번을 실행 (90도, 180도, 270도)
    for i in range(3):

        # 90도 돌기
        for r in range(N):
            for c in range(N):
                rotate_90[c][N - 1 - r] = matrix[r][c]

        # result에 값들을 넣어준다
        for idx in range(N):
            rotate = map(str, rotate_90[idx])
            r = ''.join(rotate)
            result[idx][i] = r

        # 끝나면 matrix를 rotate_90으로 초기화
        for row in range(N):
            for column in range(N):
                matrix[row][column] = rotate_90[row][column]

    print(f'#{t}')
    for r in result:
        r = ' '.join(map(str, r))
        print(r)