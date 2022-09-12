# range, sum으로도 가능

a, b = 5, 3
result = 0

if a <= b:
    for i in range(a, b + 1):
        result += i
else:
    for i in range(b, a + 1):
        result += i

print(result)