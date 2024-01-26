
while True:

    n = int(input())

    if n == -1: break

    numSum, nums = 0, []
    for i in range(1, n):
        if n % i == 0:
            numSum += i
            nums.append(i)
            
    if numSum == n:
        print(f'{n} = {" + ".join(list(map(str, nums)))}')
    else:
        print(f'{n} is NOT perfect.')