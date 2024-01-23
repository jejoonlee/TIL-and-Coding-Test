
# 조합은 같은 순서가 달라도 같은 숫자가 있으면 하나의 경우의 수다
# n개에서 r개를 순서 상관없이 r개 선택
# (1, 2)와 (2, 1)은 같다

# 순열을 r! 로 나눈 것과 같다
# nCr = nPr / r!
# nCr = n! / r!(n - r)!

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

resultP, resultR = 1, 1

for i in range(numN, (numN - numR), -1):
    print(f'n : {i}')
    resultP *= i

print(f'resultP : {resultP}')

for i in range(1, numR + 1):
    print(f'n : {i}')
    resultR *= i

resultC = int(resultP // resultR)

print(f'resultR : {resultR}')
print(f'resultC : {resultC}')