a, b = map(int, input().split())
c = int(input())

m = (a * 60 + b) + c

H = m // 60
M = m % 60

if H < 0:
    print(H + 24, M)
if H >= 24:
    print(H - 24, M)
else:
    print(H, M)