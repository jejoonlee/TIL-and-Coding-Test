a = int(input())
result = 0              # 최종 값의 초기값 생성

for i in range(0, a + 1):
    if i % 2 == 0:
        result += i     # 짝수인 i들을 result와 계속 더한다
print(result)