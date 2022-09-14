a = [1,2,3,4]
b = [-3,-1,0,2]

result = 0
for i in range(len(a)):
    result += a[i] * b[i]

print(result)