


T = int(input())

for _ in range(T):

    pay = int(input())

    # 25 10 5 1
    change = [0, 0, 0, 0]
    money = [25, 10, 5, 1]

    i = 0
    while pay > 0:

        if pay >= money[i]:
            change[i] = pay // money[i]
            pay = pay % money[i]

        i += 1

    print(' '.join(list(map(str, change))))