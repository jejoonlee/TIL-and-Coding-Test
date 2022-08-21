# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.



a = int(input())
b = 1

for i in range(0, a + 1):
    num = 2 ** i
    print(num, end = ' ')