# 여러 개의 항을 묶었을 때 규칙성을 가지는 수열
# (1/1) (1/2 2/1) (1/3 2/2 3/1) (1/4 2/3 3/2 4/1)

inputN = int(input("n항 입력 : "))

flag = True

n, nCount, searchTop, searchBtm = 1, 1, 1, 1

while flag:

    for i in range(1, (n + 1)):

        if i == n:
            print(f"{i}/{n - i + 1} ", end='')
        else:
            print(f"{i}/{n - i + 1} ", end='')

        nCount += 1

        if nCount > inputN:
            searchTop = i
            searchBtm = n - i + 1
            flag = False
            break

    print()
    n += 1

print(f"{inputN}항 : {searchTop}/{searchBtm}")