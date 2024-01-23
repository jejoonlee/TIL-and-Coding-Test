
# [동전] 앞 뒤 확률 (1/2)
# [주사위] 1, 2, 3, 4, 5, 6 (각각 1/6)



def getCombination(numN, numR) :
    # 7장 중 3장 뽑는 확률 nCr
    nPr, r = 1, 1

    for i in range(numN, numN - numR, -1):
        nPr *= i

    for i in range(1, numR + 1):
        r *= i

    nCr = int(nPr / r)

    return nCr

# 0은 모든 조합의 경우의 수, 
# 1는 꽝 2장
# 2는 선물 1장
numList = []

for i in range(3):
    numN = int(input('numN 입력 : '))
    numR = int(input('numR 입력 : '))

    nCr = getCombination(numN, numR)
    
    if i == 0:
        print(f'sample: {nCr}')
    else:
        print(f'event{i}: {nCr}')

    numList.append(nCr)

answer = (numList[1] * numList[2]) / numList[0]

print(f'probability: {round(answer * 100, 2)}%')