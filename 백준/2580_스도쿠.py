
import sys

input = sys.stdin.readline

board = [list(map(int, input().split(' '))) for _ in range(9)]

empty = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0: empty.append([i, j])


def horizontal(x, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True

def vertical(y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True

def rect(x, y, num):

    xStart, xFinish = (x // 3) * 3, (x // 3) * 3 + 3
    yStart, yFinish = (y // 3) * 3, (y // 3) * 3 + 3

    for i in range(xStart, xFinish):
        for j in range(yStart, yFinish):
            if board[i][j] == num:
                return False
    return True


def find_number(emptyIndex):

    if emptyIndex >= len(empty):
        for i in range(9):
            print(' '.join(list(map(str, board[i]))))
        exit(0)

    for num in range(1, 10): # 수도쿠는 1부터 9가 있다
        x, y = empty[emptyIndex][0], empty[emptyIndex][1]

        if horizontal(x, num) and vertical(y, num) and rect(x, y, num):
            board[x][y] = num
            find_number(emptyIndex + 1)
            board[x][y] = 0

find_number(0)

