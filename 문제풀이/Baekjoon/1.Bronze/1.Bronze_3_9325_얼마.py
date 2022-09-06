import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    # 자동차 가격 입력
    s = int(input())
    # 옵션 몇개?
    N = int(input())

    opt = 0
    for n in range(N):
        p, q = map(int, input().split())
        option = p * q
        # opt에 옵션 값 누적하기
        opt += option
    
    total = s + opt

    print(total)