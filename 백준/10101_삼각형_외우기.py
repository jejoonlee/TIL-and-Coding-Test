angles = {}
totalSum = 0

for _ in range(3):
    n = int(input())
    totalSum += n

    if n in angles:
        angles[n] += 1
    else:
        angles[n] = 1

if totalSum != 180:
    print("Error")

else:
    if len(angles) == 1:
        print("Equilateral")
    elif len(angles) == 2:
        print("Isosceles")
    elif len(angles) == 3:
        print("Scalene")
