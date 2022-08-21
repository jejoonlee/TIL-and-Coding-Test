input_ = int(input())

num = input_

cnt = 1

while True:
        a = num // 10
        b = num % 10
        c = a + b
        num = b * 10 + c % 10
        if num != input_:
            cnt += 1
        elif num == input_:
            break

print(cnt)