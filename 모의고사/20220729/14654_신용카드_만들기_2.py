
T = int(input())

lst = []
for i in range(1, T + 1):
    nums = (str(input()))
    nums = list(nums.replace('-',''))

    lst = []
    if nums[0] == '3' or nums[0] == '4' or nums[0] == '5' or nums[0] == '6' or nums[0] == '9':
        lst.append(nums)
    else:
        print(f'#{i} 0')


    for valid in lst:
        if len(valid) == 16:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')