
def get_sosu():
    sosu = [0] * 1001
    sosu[0], sosu[1] = 1, 1

    for i in range(2, 500):

        for j in range(i + i, 1001, i):
            if sosu[j] == 0:
                sosu[j] = 1

    return sosu

def get_input():
    n = int(input())
    nList = list(map(int, input().split(' ')))

    return nList

sosu = get_sosu()

count = 0

for num in get_input():
    if sosu[num] == 0:
        count += 1

print(count)