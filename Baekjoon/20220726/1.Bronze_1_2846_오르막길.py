n = int(input())

a = list(map(int, input().split()))

up = []
incline = 0

for i in range(1, n):
    if a[i] > a[i - 1]:
        incline += a[i] - a[i - 1]
        up.append(incline)
    else:
        incline = 0
        up.append(incline)
print(max(up))