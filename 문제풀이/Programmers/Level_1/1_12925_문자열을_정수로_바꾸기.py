
s = '-1234'
result = 0

for idx, num in enumerate(s[::-1]):
    if num == '-':
        result *= -1
    else:
        result += int(num) * (10 ** idx)
    
print(result)