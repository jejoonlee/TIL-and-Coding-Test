import sys

sys.stdin = open("_반반.txt")

T = int(input())

for t in range(1, T + 1):
    S = input()

    al_cnt = {}

    for s in S:
        if s in al_cnt:
            al_cnt[s] += 1
        else:
            al_cnt[s] = 1
    
    # result 안에 value 값이 2인 key가
    # 2개가 있으면 참이고, 그 외는 거짓이다
    result = []
    for key, value in al_cnt.items():
        if value == 2:
            result.append(key)

    if len(result) == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')