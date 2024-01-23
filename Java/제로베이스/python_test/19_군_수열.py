# 여러 개의 항을 묶었을 때 규칙성을 가지는 수열
# 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5
# (1) (1, 2) (1, 2, 3) (1, 2, 3, 4) (1, 2, 3, 4, 5)

inputN = int(input("n항 입력 : "))

flag = True

# nCount는 항의 자리
n, nCount, searchN = 1, 1, 0

while flag:
    for i in range(1, (n + 1)):
        if i == n:
            print(f"{i}", end="")

        else:
            print(f"{i}, ", end="")

        nCount += 1

        if nCount > inputN:
            flag = False
            searchN = i
            break

    print()
    n += 1
