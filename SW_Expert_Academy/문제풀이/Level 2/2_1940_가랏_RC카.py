import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    # 이동한 시간 입력
    N = int(input())

    speed = 0
    distance = 0

    for n in range(N):
        # command[0]
        # 0 = 현재 속도 유지
        # 1 = 가속
        # 2 = 감속

        # command[1]
        # 얼마나 가속하는지 아님 감속하는지 1 또는 2
        command = list(map(int, input().split()))

        if command[0] == 1:
            if speed >= 0:
                speed += command[1]
        if command[0] == 2:
            if speed > 0:
                speed -= command[1] 

        distance += speed
    
    print(f'#{t} {distance}')