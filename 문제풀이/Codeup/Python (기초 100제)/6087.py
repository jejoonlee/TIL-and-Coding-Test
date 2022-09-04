a = int(input())
b = 0

while a > b:
    b += 1
    if b % 3 == 0:
        continue        # 3의 배수는 건너뛰고, 계속 출력한다
    print(b, end = ' ')