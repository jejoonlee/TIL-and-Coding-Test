
num1 = int(input())
num2 = int(input())

a, b = num1, num2

print(a * (b % 10))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)