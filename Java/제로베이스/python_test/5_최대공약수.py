# 두 개 이상의 수에서 공통된 약수를 공약수이다
# 그 중에서 제일 큰 수가 최대공약수다

inputNum = int(input(f'1보다 큰 숫자를 넣으세요 : '))
inputNum2 = int(input(f'두번째 1보다 큰 숫자를 넣으세요 : '))

# n = 2
answer = 1

# while n <= inputNum:
#     if inputNum % n == 0 and inputNum2 % n == 0:
#         answer *= n
#         inputNum /= n
#         inputNum2 /= n

#     else:
#         n += 1

for num in range(1, inputNum + 1):
    if inputNum % num == 0 and inputNum2 % num == 0:
        print(f'공약수 : {num}')
        answer = num

print(f'최대공약수 : {answer}')