a, r, n = map(int, input().split())

# result = a * (r ** (n - 1))

# print(result)

for i in range(1, n):   # n - 1번
    a = a * r

print(a)