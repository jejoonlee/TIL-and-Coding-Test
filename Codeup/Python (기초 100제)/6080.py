a, b = map(int, input().split())

for i in range(1, a + 1):       # 1이상 a+1 미만
    for j in range(1, b + 1):   # 1이상 b+1 미만
        print(i, j)