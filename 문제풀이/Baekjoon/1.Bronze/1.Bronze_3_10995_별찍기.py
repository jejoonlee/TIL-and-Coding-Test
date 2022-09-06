num = int(input())


for i in range(1, num + 1):
# i 는 num개의 줄을 출력해준다
    if i % 2 == 1:
    # i 가 홀수 줄이면 '* ' 을 num 값만큼 출력해준다
    # 여기서 별 다음에 공간을 줄 것
        print(num * '* ')
    else:
    # 반대로 i가 짝수 줄이면 ' *'을 num 값만큼 출력해준다
    # 다른 것은 공간을 먼저 주고, 별을 찍어준다
        print(num * ' *')
