# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

a = int(input())
result = 0

while a > 0:
    last = a % 10                  # a 를 10으로 나누고, 나눈 나머지
    result = result * 10 + last    # 결과값을 10으로 곱하고, last를 맨 뒤로 보낸다
    a = a // 10                    # a 의 몫을 반환한다.

print(result)


# 1. a 가 0보다 크면
# 2. a를 10으로 나누고, 남은 값을 반환한다 (last의 값)
# 3. result는 0으로 시작하고, last의 값을 더한다 (두번째면 result의 값은 10을 곱하기 때문에 2자리 수가 된다)
# 4. a를 나누고, 나오는 몫을 반환하고, 위로 보낸다

# 예)
#                               a  =          123             12                 1
#     last = a % 10                 |    last:  3 |     last:   2 |     last:    1  |
#     result = result * 10 + last   |  result:  3 |   result:  32 |   result:  321  |
#     a = a // 10                   |       a: 12 |        a:   1 |        a:    0  |