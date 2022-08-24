import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    nums = sorted(list(map(int, input().split())))
    
    num = sum(nums[1:9])
    result = num / len(nums[1:9])

    print(f'#{t} {round(result)}')