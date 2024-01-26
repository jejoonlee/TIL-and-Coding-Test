
n = int(input())

num = [1]
count, add = 1, 6

while count <= 1000000000:

    if n > count:
        count += add
        num.append(count)
        add += 6
    else:
        break

print(len(num))