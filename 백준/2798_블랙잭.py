from itertools import combinations

n, m = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

answer = 0

for i in combinations(cards, 3):

    temp = sum(i)
    if temp <= m and temp > answer:
        answer = temp

print(answer)
