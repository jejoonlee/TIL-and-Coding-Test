import sys

sys.stdin = open('input.txt')

# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

T = int(input())


for i in range(1, T + 1):
    result = 0
    # 결과 변수를 0으로 기본값을 정한다
    a = list(map(int, input().split()))
    # a 변수는 입력값을 int로 변환 후 리스트 안에 넣어준다
    for num in a:
    # 리스트 안에 있던 수들을 num 변수를 통해 반환한다
        if num % 2 != 0:
        # 홀수인 num 정수는
            result += num
            # result 변수에 더해준다
    print(f'#{i}', result)
    