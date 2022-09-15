import sys
sys.stdin = open('input.txt')

# 원래 호텔 기준을 시계방향으로 90도를 돌려서 풀이
# 그러면 층수 (앞에 숫자)가 column이 되고
# 방의 호수 (위의 숫자) 가 row가 된다

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    cnt = 0
    flag = False

    for column in range(1, W + 1):
        for row in range(1, H + 1):
            cnt += 1
            if cnt == N:
                flag = True
                break
        
        if flag == True:
            break

    # 인덱스는 0부터 시작함으로 column에 1을 더하고
    # row는 break 하기 전에 이미 한번 더 for문을 거쳐가기 때문에,
    # 추가로 더할 필요가 없다
    if column < 10:
        print(f'{row}0{column}')
    else:
        print(f'{row}{column}')