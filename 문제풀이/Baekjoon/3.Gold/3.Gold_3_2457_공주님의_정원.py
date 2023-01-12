import sys
sys.stdin = open("input.txt")

month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

# 공주가 좋아하는 계절
princess_flower = (60, 334)

N = int(input())

flower = []

for _ in range(N):
    month_1, day_1, month_2, day_2 = map(int, input().split())
    range_1 = month[month_1 - 1] + day_1
    range_2 = month[month_2 - 1] + day_2
    flower.append((range_1, range_2))

flower.sort(key = lambda x: (x[0], -x[1]))
print(flower)

temp = 0

# for period in flower:
#     if period[0] <= princess_flower[0] and period[0] > temp:
#         temp = period[1]


# print(flower)
