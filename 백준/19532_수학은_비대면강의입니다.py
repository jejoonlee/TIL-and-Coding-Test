
a, b, c, d, e, f = map(int, input().split(' '))


x = ((e * c) - (b * f)) // ((e * a) - (b * d))
y = ((d * c) - (a * f)) // ((d * b) - (a * e))

print(x, y)