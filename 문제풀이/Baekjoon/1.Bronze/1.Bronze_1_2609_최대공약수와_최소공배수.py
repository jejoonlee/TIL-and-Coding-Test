# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())

for i in range(min(a,b), 0, -1):
    if (a % i == 0) and (b % i == 0):
        print(i)
        break

for i in range(max(a,b),(a * b) + 1):
    if (i % a == 0) and (i % b == 0):
        print(i)
        break