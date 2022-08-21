import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    num = int(input())
    dist = list(map(int, input().split()))
    
    dif_num = set()
    for d in dist:
        dif = abs(d - 0)
        # 0과 던진 돌의 차이를 구한다
        dif_num.add(dif)
        # set에 차이들을 넣는다. 겹치면 없어짐
        close = min(dif_num)
    
    p_num = []

    for r in dist:
        if abs(r) == close:
            p_num.append(r)

    print(f'#{t} {close} {len(p_num)}')