

paper = int(input())

space = [[0] * 100 for _ in range(100)]

count = 0

for _ in range(paper):
    x, y = map(int, input().split())

    for i in range(x, x + 10):

        for j in range(y, y + 10):

            if space[i][j] == 0:
                space[i][j] = 1
                count += 1

print(count)