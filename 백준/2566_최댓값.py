

def input_matrix():
    matrix = []

    for _ in range(9):
        nums = list(map(int, input().split(' ')))
        matrix.append(nums)

    return matrix


def search_max(matrix):

    findNums = [-1] * 3 # 최대수, 행 위치, 열 위치

    for i in range(9):
        for j in range(9):
            if matrix[i][j] > findNums[0]:
                findNums[0], findNums[1], findNums[2] = matrix[i][j] ,i + 1, j + 1

    return findNums

matrix = input_matrix()
answer = search_max(matrix)

print(answer[0])
print(f'{answer[1]} {answer[2]}')