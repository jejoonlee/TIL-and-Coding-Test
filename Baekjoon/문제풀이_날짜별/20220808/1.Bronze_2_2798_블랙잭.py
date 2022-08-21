import sys
sys.stdin = open('input.txt', 'r')

# N 장의 카드, N장의 카드중 3개를 고른다
# M 이라는 숫자. M이라는 숫자와 같거나 최대한 가깝게

N, M = map(int, input().split())

cards = list(map(int, input().split()))

max_num = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            # 3중문으로 한번씩 더해준다
            num = cards[i] + cards[j] + cards[k]

            # M보다 작을 경우는 계속 위의 공식을 진행한다
            if max_num < num <= M:
                # num이 max_num보다 크면 max_num은 num의 값이 된다
                max_num = num

print(max_num)