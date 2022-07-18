a = int(input())
b = 0

for i in range(1, a + 1):
    b += i
    if b >= a:      # b가 a와 같아지거나, 커지면
        print(b)
        break       # 중단한다
