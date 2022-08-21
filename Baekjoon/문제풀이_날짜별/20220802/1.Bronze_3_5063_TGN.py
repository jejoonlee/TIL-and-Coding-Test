

N = int(input())

for n in range(N):
    r, e, c = map(int, input().split())
    total = e - c
    # e는 수익, c는 비용, r은 아무것도 안 했을 때의 수익
    if total > r:
        print('advertise')
    elif total == r:
        print('does not matter')
    else:
        print('do not advertise')
