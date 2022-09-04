t = int(input())

for i in range(1, t + 1): 
    a = int(input())
    result = 0                  # result가 for문의 안 쪽으로 있어야, 0으로 초기된다. ***
    for idx in range(1, a + 1):
        if idx % 2 == 0:
            result -= idx
        else:
            result += idx
    print(f'#{i}', result)
