
for _ in range(int(input())):

    n, x, y = map(int, input().split(' '))
    array = list(map(int, input().split(' ')))

    count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (array[i] + array[j]) % x == 0 and (array[i] - array[j]) % y == 0:
                count += 1

    print(count)