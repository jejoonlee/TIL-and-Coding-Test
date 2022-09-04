import sys
sys.stdin = open('input.txt')

# 길이가 적은 변수 기준으로 움직여야 한다

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # length라는 변수는 길이가 더 적은 변수 기준의 길이를 구한다
    if N > M:
        length = M
    else:
        length = N

    # 길이가 더 짧은 변수가, 몇번을 움직이면서 
    # 계산을 해야하는지 move 통해 구한다
    move = abs(N - M) + 1

    max_count = 0

    # move번을 움직인다
    for m in range(move):
        cnt = 0


        for i in range(length):
            # 조건문을 통해, 길이가 짧은 변수 기준으로
            # 계산을 하는 것을 명시한다
            # 만약에 조건문이 없을 경우 리스트 밖으로 나갈 수 있다
            if N <= M:
                cnt += A[i] * B[i + m]
            else:
                cnt += B[i] * A[i + m]
        
        # 최대 값 구하기
        if cnt > max_count:
            max_count = cnt
    
    print(f'#{t} {max_count}')