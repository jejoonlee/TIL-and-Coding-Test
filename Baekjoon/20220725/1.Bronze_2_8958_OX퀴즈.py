# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())

# 'sum'과 'result'를 0으로 설정
# 'X' 값이면 'sum'은 바로 0으로 반환된다
# 'O' 값이면 'sum += 1' 을 통해 O는 1이 되고
# 'O' 값이 반복하면 'sum += 1' 을 통해 1씩 더해진다
# 'result += sum' 은 'sum' 변수를 더하고 나온 결과 값이다
for i in range(1, t + 1):
    a = list(input())
    num = 0
    result = 0
    for i in a:
        if i == 'O':
            num += 1
            result += num
        elif i == 'X':
            num = 0
    
    print(result)
