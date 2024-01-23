import random

# 100부터 1000 사이의 난수에 대해서 약수, 소수, 그리고 소인수를 출력
# 난수 = random

n = random.randint(100, 1000)

yak = []
sosuAns = []
soInSu = []
# 소수면 0
sosu = [0] * (n + 1)

for i in range(1, n + 1):
    if n % i == 0:
        yak.append(i)

sosu[0], sosu[1] = 1, 1
for i in range(2, n // 2 + 1):
    
    for k in range(i + i, n + 1, i):
        if sosu[k] == 0:
            sosu[k] = 1

for i in range(2, n + 1):
    if sosu[i] == 0:
        sosuAns.append(i)

        if n % i == 0:
            soInSu.append(i)

print(f'약수 : {yak}')
print(f'소수 : {sosuAns}')
print(f'소인수 : {soInSu}')