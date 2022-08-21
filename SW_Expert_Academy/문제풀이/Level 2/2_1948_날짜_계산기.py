import sys
sys.stdin = open('input.txt')

# 1월 1일부터 해당 날짜들의 일수를 구한 다음
# 그 수를 빼고 난 후 1을 더하면 두 날짜의 차이가 나온다

T = int(input())

for t in range(1, T + 1):
    days = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,
    }

    m, d, m1, d1 = map(int, input().split())

    date = 0
    for i in range(1, m1):
        date += days[i]

    end_date = date + d1

    date1 = 0
    for j in range(1, m):
        date1 += days[j]

    start_date = date1 + d

    result = (end_date - start_date) + 1

    print(f'#{t} {result}')