
# a1 + (n-1) * d
# a1은 첫 숫자, d는 숫자들 사이의 차이

inputNum1 = int(input('a1 입력 : '))
inputD = int(input('공차 입력 : '))
inputN = int(input('n 입력 : '))

numVal = inputNum1
n = 1

while n <= inputN:

    print(f'{n}번째 항의 값 : {numVal}')

    numVal += inputD 
    n += 1


# n번째 항의 숫자 찾기!
# a1 + (n-1) * d
print(f'{inputN}번째 항의 값 : {inputNum1 + (inputN - 1) * inputD}')