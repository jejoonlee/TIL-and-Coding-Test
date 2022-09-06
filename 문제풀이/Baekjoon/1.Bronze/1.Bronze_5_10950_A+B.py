# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

t = int(input())

# 't'를 입력하고, for문으로 range와 같이 쓰면
# 't'의 입력 값은, 몇 번의 계산을 하는지 알려준다.
# range를 통해 't'번의 계산을 해준다
for tests in range(1, t + 1):
    a, b = map(int, input().split())
    # a와 b의 int값들을 입력
    ans = a + b
    print(ans)
    # input()이 입력될때마다, 출력을 해준다