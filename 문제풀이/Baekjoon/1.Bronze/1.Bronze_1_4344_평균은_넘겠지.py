import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = list(map(int, input().split()))

    scores = []
    # 점수만 있는 리스트
    for i in range(1, len(N)):
        scores.append(N[i])

    # 평균을 구한다
    ave = sum(scores) / N[0]

    # 평균을 넘는 학생들의 수를 구한 후
    above = []
    for i in scores:
        if i > ave:
            above.append(i)

    # 넘는 학생들의 수 / 학생 수
    per = (len(above) / N[0]) * 100
    result = '{:.3f}'.format(per)

    # '{:.3f}'.format(value) 를 써서 소수점 조정하기

    print(f'{result}%')