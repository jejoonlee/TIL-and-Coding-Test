
n = int(input())


i, add, total = 0, 1, 2

while i < n:

    i += 1
    total += add
    add *= 2

    

print(total ** 2)