
def get_sosu():
    sosu = [0] * 10001
    sosu[0], sosu[1] = 1, 1

    for i in range(2, 5001):
        for j in range(i + i, 10001, i):
            if sosu[j] == 0:
                sosu[j] = 1

    return sosu

def get_lowest_add(sosu):
    m, n = int(input()), int(input())
    answer = [0, 0]

    for i in range(m, n + 1):
        if sosu[i] == 0:
            answer[0] += i
        
        if sosu[i] == 0 and answer[1] == 0:
            answer[1] = i

    return answer

sosu = get_sosu()

for num in get_lowest_add(sosu):
    if num == 0:
        print(-1)
        break
    print(num)