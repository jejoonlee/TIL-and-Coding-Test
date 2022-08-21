
import sys
sys.stdin = open('input.txt', 'r')

matrix = [[0] * 100 for _ in range(100)]
# 100 * 100 행렬을 만든다

place = []
for _ in range(4):
    x, y, x_1, y_1 = map(int, input().split())
    # 입력값을 x, y, x_1, y_1로 받는다
    for i in range(x, x_1):
    # i는 입력값의 x부터 x_1 미만이다
        for j in range(y, y_1):
        # j는 입력값 y부터 y_1 미만이다
            matrix[i][j] = 1

# x, x_1 / i, i_1 을 한 이유는 행열이 아니라 좌표로만 보아도
# (x_1 - x) * (i_1 - i) 로 각 직사각형의 면적을 구할 수 있다
# 즉 x, x_1 / i, i_1은 직사각형의 면적을 구하되, 각 행열마다,
# 1만 넣어서, 겹치는 행열마저도 1로 만들 수 있다

print(sum(map(sum, matrix)))