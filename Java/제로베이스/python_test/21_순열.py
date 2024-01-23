# 순열은 일렬로 나열하는 수
# n개에서 r개를 택하여 나열하는 경우의 수
# 숫자가 같아도, 순서가 다르면, 다른 것이다

# nPr = n! / (n - r)!

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

ans = 1

for i in range(numN, (numN - numR), - 1):
    print(f"n : {i}")
    ans *= i

print(f"result : {ans}")