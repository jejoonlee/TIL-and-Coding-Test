import sys
sys.stdin = open('input.txt', 'r')

triangle = []

for i in range(3):
    angle = int(input())
    triangle.append(angle)


if sum(triangle) != 180:
    print('Error')
else:
    if len(set(triangle)) == 3:
        print('Scalene')
    elif len(set(triangle)) == 2:
        print('Isosceles')
    elif len(set(triangle)) == 1:
        print('Equilateral')