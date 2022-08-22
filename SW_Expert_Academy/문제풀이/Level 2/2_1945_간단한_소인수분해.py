# import sys
# sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = [2, 3, 5, 7, 11]
    num = int(input())

    result = []

    for i in range(len(N)):
        cnt = 0
        while True:
            if num % N[i] == 0:
                num = num / N[i]
                cnt += 1
            else:
                break
            
        result.append(cnt)

    result = list(map(str, result))
    result = ' '.join(result)

    print(f'#{t} {result}')


# 수소 구하기 100까지 수 중에서

N = 100
cnt = 0

while cnt != N:
    cnt += 1
    divide = []
    for i in range(1, cnt + 1):
        if cnt % i == 0:
            divide.append(i)
    
    if len(divide) == 2:
        print(cnt)
    else:
        continue