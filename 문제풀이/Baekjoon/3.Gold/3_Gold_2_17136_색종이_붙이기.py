import sys

sys.stdin = open("input.txt")

matrix = [list(map(int, input().split())) for _ in range(10)]

count = [0] * 6

ans = 25

def is_possible(i, j, size):
    if count[size] == 5:
        return False

    if i + size > 10 or j + size > 10:
        return False

    for r in range(size):
        for c in range(size):
            if matrix[i + r][j + c] == 0:
                return False

    return True


def mark(i, j, size, fill):
    for r in range(size):
        for c in range(size):
            matrix[i + r][j + c] = fill

    if fill == 0:
        count[size] += 1
    else:
        count[size] -= 1


def backtrack(i, j):

    global ans

    if i == 10:
        ans = min(ans, sum(count))
        return

    if j == 10:
        backtrack(i + 1, 0)
        return

    if matrix[i][j] == 0:
        backtrack(i, j + 1)
        return

    for size in range(1, 6):
        if is_possible(i, j, size):
            mark(i, j, size, 0)
            backtrack(i, j + 1)
            mark(i, j, size, 1)


backtrack(0, 0)
print(-1 if ans == 25 else ans)