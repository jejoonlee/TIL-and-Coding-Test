
chess = [1, 1, 2, 2, 2, 8]

a = list(map(int, input().split()))

need = []
for i in range(len(chess)):
    gone = chess[i] - a[i]
    need.append(gone)

print(*need)