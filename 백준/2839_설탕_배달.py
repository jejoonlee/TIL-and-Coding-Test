
def bag():

    n = int(input())

    start = n // 5

    for i in range(start, -1, -1):
        if i * 5 == n:
            return i
        else:
            tempNum = n - (5 * i)

            if tempNum % 3 == 0:
                return i + tempNum // 3
            
    if n % 3 == 0: return n // 3
    else: return -1

print(bag())