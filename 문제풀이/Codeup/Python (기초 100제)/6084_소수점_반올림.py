h, b, c, s = map(float, input().split())

result = (h * b * c * s) / 2 ** 23

print(round(result, 1), 'MB', sep=' ')

# round() 소수점 반올림