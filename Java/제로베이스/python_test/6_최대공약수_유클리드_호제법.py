# 12와 36의 최대공약수 구하기
# 12 % 39 = 12
# 39 % 12 = 3
# 12 % 3 = 0 (3이 최대공약수)

num1 = int(input("1보다 큰 정수 입력 : "))
num2 = int(input("1보다 큰 정수 입력 : "))

temp1, temp2 = num1, num2

while temp1 % temp2 != 0:
    tempNum = temp1 % temp2
    temp1 = temp2
    temp2 = tempNum

print(f"{num1}의 {num2} 최대공약수 : {temp2}")

for n in range(1, temp2 + 1):
    if temp2 % n == 0:
        print(f'{num1}, {num2}의 공약수 : {n}')