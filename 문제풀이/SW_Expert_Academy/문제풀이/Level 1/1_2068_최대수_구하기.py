# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

T = int(input())

for i in range(1, T + 1):
    a = list(map(int, input().split()))
    # a변수는, 입력하는 str을 int로 변환하고
    # 변환된 수들을 list 안에다 넣는다
    print(f'#{i}', max(a))
    # list 안에 있는 숫자들을 비교해 max(a) 최댓값을 구한다