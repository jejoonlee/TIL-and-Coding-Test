T = int(input())

for t in range(1, T + 1):
    num = map(int, input().split())
    nums = list(num)

    result = 0
    for i in range(len(nums)):
        if (i) % 2 == 1:
            result += nums[i]
        else:
            result += (nums[i] * 2)
    

    if result % 10 == 0:
        print(f'#{t} 0')
    else:
        print(f'#{t} {10 - result % 10}')

    
