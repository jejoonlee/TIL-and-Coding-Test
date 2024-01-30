from itertools import combinations

# n, m = map(int, input().split(' '))
# cards = list(map(int, input().split(' ')))

# answer = 0

# for i in combinations(cards, 3):

#     temp = sum(i)
#     if temp <= m and temp > answer:
#         answer = temp

# print(answer)

cards = [1, 2, 3, 4, 5]

def combi(idx, array, limit):

    if len(array) >= limit:
        print(array)
        return
    
    for i in range(idx, len(cards)):
        combi(i + 1, array + [cards[i]], limit)

combi(0, [], 3)