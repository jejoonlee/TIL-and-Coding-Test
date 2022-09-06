# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


while True:
    A, B = map(int, input().split())
    # while 문이 계속 돌아갈 때, A와 B의 input을 지속적을 넣어준다
    ans = A + B
    if ans == 0:
    # ans 값이 0이면, break 즉 while문을 종료한다
        break
    print(ans)