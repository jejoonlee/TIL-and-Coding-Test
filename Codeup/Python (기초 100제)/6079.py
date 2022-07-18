a = int(input())
b = 0

for i in range(1, a + 1):
    b += i          # i에서 반환된 것들을 더하기
    if b >= a:      # 더하다가 b가 a와 똑같거나 커지면
        print(i)    # 해당 i를 출력해라
        break