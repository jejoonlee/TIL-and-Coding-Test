t = int(input())


def distribute(n, container):

    wLvl = sum(container) // n

    left, right = 0, 1

    while right < n:
        give = container[left] - wLvl

        if give < 0:
            return False

        elif container[left] >= container[right]:
            container[right] += give
            container[left] = wLvl
            left, right = left + 1, left + 2

        right += 1

    for num in container:
        if num != wLvl:
            return False

    return True


for _ in range(t):

    n, container = int(input()), list(map(int, input().split(" ")))

    if n == 1:
        print("YES")

    else:
        if sum(container) % n != 0:
            print("NO")

        else:
            if distribute(n, container):
                print("YES")
            else:
                print("NO")
