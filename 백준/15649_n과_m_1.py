import sys


def combi(array, idx, answer, limit):

    if len(answer) >= limit:
        print(' '.join(list(map(str, answer))))
        return

    for i in range(0, len(array)):
        if visited[i] == 0:
            visited[i] = 1
            combi(array, idx + 1, answer + [array[i]], limit)
            visited[i] = 0


n, m = map(int, input().split(" "))

visited = [0] * n

combi(list(range(1, n + 1)), 0, [], m)
