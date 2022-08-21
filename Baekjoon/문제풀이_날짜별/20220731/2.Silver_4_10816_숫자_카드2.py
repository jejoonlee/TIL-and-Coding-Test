

# 가지고 있는 카드의 정수
N = int(input())
N_card = input().split()
# 구해야할 카드 M개의 정수
M = int(input())
M_card = input().split()

# 방식 1. M_card를 먼저 딕셔너리에 넣고
# N_card랑 같은 숫자면 1을 더하고, 없으면 그냥 놔두기

# card = {}
# for i in M_card:
#     if i not in card:
#         card[i] = 0

# for i in N_card:
#     if i in card:
#         card[i] += 1
#     else:
#         continue

# result = list(card.values())

# for i in result:
#     print(i, end = ' ')


card = {}
for n in N_card:
    if n not in card:
        card[n] = 1
    else:
        card[n] += 1

for m in M_card:
    if m in card:
        print(card[m], end = ' ')
    else:
        print(0, end =' ')
