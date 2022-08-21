
# A사 : W * P원
# B사 :
#   R이하 : Q
#   R초과 : Q + S * (W-R)


t = int(input())

for i in range(1, t+1):
    P, Q, R ,S, W = map(int, input().split())
    A = P * W           # A의 수도요금은 P 곱하기 W
    if W <= R:          # B는 R리터 이하를 이용하면
        B = Q           # B의 요금은 Q
    else:
        B = (W - R) * S + Q # 그게 아닌경우 Q리터 더하기 1리터당 S원
    if A < B:
        print(f'#{i}', A)
    else:
        print(f'#{i}', B)


t = int(input())

for i in range(1, t+1):
    P, Q, R ,S, W = map(int, input().split())
    A = P * W           # A의 수도요금은 P 곱하기 W
    if W <= R:          # B는 R리터 이하를 이용하면
        B = Q           # B의 요금은 Q
    else:
        B = (W - R) * S + Q # 그게 아닌경우 Q리터 더하기 1리터당 S원
    if A < B:
        print(f'#{i}', A)
    else:
        print(f'#{i}', B)