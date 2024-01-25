n, m = map(int, input().split(" "))


matrixOne = []
matrixTwo = []
answer = [[0] * m for _ in range(n)]

for _ in range(n):
    nums = list(map(int, input().split(" ")))
    matrixOne.append(nums)

for _ in range(n):
    nums = list(map(int, input().split(" ")))
    matrixTwo.append(nums)

for i in range(n):
    for j in range(m):
        answer[i][j] = matrixOne[i][j] + matrixTwo[i][j]

for i in range(n):
    print(" ".join(map(str, answer[i])))
