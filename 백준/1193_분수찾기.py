
x = int(input())

i = 1
numSum = 0

while numSum < x:

    numSum += i
    i += 1

i -= 1
numX = 1

for _ in range(numSum - i + 1, x):
    numX += 1

if i % 2 == 0:
    print(f'{numX}/{i - numX + 1}')

else:
    print(f'{i - numX + 1}/{numX}')