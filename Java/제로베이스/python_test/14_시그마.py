
# 시그마는 수열의 합을 나타내는 기호다 Σ

# 일반항 공식
# an = a1 + (n - 1)d

# 수열의 합 
# sn = n(a1 + an) / 2

inputN1 = int(input('a1 입력 : '))
inputDorR = int(input('공차 입력 : '))
inputN = int(input('n 입력 : '))

valueN = inputN1 + (inputN - 1) * inputDorR
sumN = (inputN * (inputN1 + valueN)) // 2

print(f'{inputN}번째 항까지의 합 : {sumN}')

# 등비 수열의 합
# sn = a1 * (1 - r ^ n) / (1 - r)

valueR = (inputN1 * (1 - inputDorR ** inputN)) // (1 - inputDorR)
print(f'{inputN}번째 항까지의 합 : {valueR}')