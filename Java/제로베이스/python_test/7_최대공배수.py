
# 공통된 배수
num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

temp1, temp2 = num1, num2
maxNum = 1

for n in range(1, num1 + 1):
    if num1 % n == 0 and num2 % n == 0:
        print(f'공약수 : {n}')
        maxNum = n

minNum = (num1 * num2) // maxNum

print(f'최대공약수 : {maxNum}')
print(f'최대공배수 : {minNum}')