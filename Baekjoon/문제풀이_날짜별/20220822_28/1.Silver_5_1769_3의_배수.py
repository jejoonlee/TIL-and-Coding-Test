

def three_mult(N, cnt):
    if len(N) == 1:
        if N[0] % 3 == 0:
            return (cnt, 'YES')
        else:
            return (cnt, 'NO')

    else:
        cnt += 1
        N = list(map(int, str(sum(N))))
        return three_mult(N, cnt)

nums = [1, 2, 3, 4, 5, 6, 7]

for i in three_mult(list(map(int, input())), 0):
    print(i)