
nums = int(input())

cnt = 0

for num in range(1, nums + 1):
    if num < 100:
        cnt += 1

    # else: 
    #     num = list(map(int, str(num)))
    #     if num[0] - num[1] == num[1] - num[2]:
    #         cnt += 1

    else:
        num = list(map(int, str(num)))
        for i in range(len(num)):
            if num[i] - num[i + 1] == num[i + 1] - num[i + 2]:
                cnt += 1

print(cnt)