import sys
sys.stdin = open('input.txt')

#시간 초과
# T = int(input())

# for t in range(1, T + 1):

#     N = int(input())

#     money = {
#         50000 : 0,
#         10000 : 0,
#         5000 : 0,
#         1000 : 0,
#         500 : 0,
#         100 : 0,
#         50 : 0,
#         10 : 0
#     }

#     # N이 0이 될때까지 계산을 한다
#     while N != 0:
#         # money 딕셔너리에서 50000원, 10000원, 5000원...
#         # 의 key와 value를 한번씩 가지고 온다
#         for key, value in money.items():
#             # 만약 N이 key보다 작으면 for문으로 가서 
#             # 지폐 한 단계 아래를 가지고 온다
#             if key > N:
#                 continue
#             # N이 key보다 크면, 먼저 N을 몇개를 써야하는지
#             # 1. N과 key의 몫을 구한다. 몫을 딕셔너리에 저장
#             # 2. key를 몫 만큼 N을 빼준다.
#             else:
#                 count = N // key
#                 money[key] = count
#                 N = N - (key * count)
                

#     change = []
#     for key, value in money.items():
#         change.append(value)

#     print(f'#{t}')
#     print(*change)

# 시간 초과
# T = int(input())

# for t in range(1, T + 1):

#     N = int(input())

#     money = {
#         50000 : 0,
#         10000 : 0,
#         5000 : 0,
#         1000 : 0,
#         500 : 0,
#         100 : 0,
#         50 : 0,
#         10 : 0
#     }

#     while N != 0:
#         for key in money:
#             if key > N:
#                 continue
#             else:
#                 count = N // key
#                 money[key] = count
#                 N = N - (key * count)
                

#     change = []
#     for k in money:
#         change.append(money[k])

#     print(f'#{t}')
#     print(*change)


# 리스트 이용하기
# # 시간 초과;;;
# T = int(input())
# for t in range(1, T + 1):

#     N = int(input())

#     money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#     quantity = [0] * 8

#     while N != 0:
#         for i in range(len(money)):
#             count = 0
#             if money[i] > N:
#                 quantity[i] = count
#                 continue
#             else:
#                 count = N // money[i]
#                 quantity[i] = count
#                 N = N - (money[i] * count)

#     print(f'#{t}')
#     quantity = ' '.join(map(str, quantity))
#     print(quantity)

# while문 빼기
T = int(input())
for t in range(1, T + 1):

    N = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    quantity = [0] * 8

    for i in range(len(money)):
        cnt = 0
        if N // money[i] != 0:
            cnt = N // money[i]
            quantity[i] = cnt
            N = N - (cnt * money[i])

    print(f'#{t}')
    quantity = ' '.join(map(str, quantity))
    print(quantity)

# 딕셔너리로 풀어보기
T = int(input())
for t in range(1, T + 1):

    N = int(input())

    money = {
        50000 : 0,
        10000 : 0,
        5000 : 0,
        1000 : 0,
        500 : 0,
        100 : 0,
        50 : 0,
        10 : 0
    }

    for i in money:
        cnt = 0
        if N // i != 0:
            cnt = N // i
            money[i] = cnt
            N = N - (cnt * i)

    print(f'#{t}')
    print(*money.values())
