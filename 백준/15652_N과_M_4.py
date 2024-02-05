import sys

input = sys.stdin.readline


def permut(array, result, idx, limit):

    if len(result) >= limit:
        print(' '.join(list(map(str, result))))
        return

    for i in range(0, len(array)):

        if len(result) == 0 or (len(result) > 0 and array[i] >= result[idx - 1]):

            permut(array, result + [array[i]], idx + 1, limit)


n, m = map(int, input().split(" "))
permut(list(range(1, n + 1)), [], 0, m)
