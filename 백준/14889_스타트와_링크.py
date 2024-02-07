
import sys

input = sys.stdin.readline


def combi(idx, array, limit):

    global result

    if len(array) == limit:
        result = min(abs(check_dif(array)), result)
        return
    
    for i in range(idx, len(players)):
        combi(i + 1, array + [players[i]], limit)

def check_dif(array):

    setOne = set(array)
    setTwo = set(players) - setOne
    arrayTwo = list(setTwo)

    teamStart, teamLink = 0, 0

    for i in range(len(setOne)):
        for j in range(i + 1, len(setOne)):
            x1, y1 = array[i], array[j]
            x2, y2 = arrayTwo[i], arrayTwo[j]
            teamStart += scores[x1][y1] + scores[y1][x1]
            teamLink += scores[x2][y2] + scores[y2][x2]
    
    return teamStart - teamLink


n = int(input())

players = list(range(0, n))

scores = [list(map(int, input().split(' '))) for _ in range(n)]

result = 10 ** 10

combi(0, [], n // 2)

print(result)