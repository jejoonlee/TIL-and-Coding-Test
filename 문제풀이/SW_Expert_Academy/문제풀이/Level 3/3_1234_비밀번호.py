import sys
sys.stdin = open('input.txt')

# 같은 숫자가 연속으로 붙어있으면 없애는 것
# 없애는 과정에서 연속으로 똑같은 숫자가 붙을 수 있음

for t in range(1, 11):

    inp = input().split()

    nums = list(map(int, list(inp[1])))

    i = 0

    while len(nums) != i + 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
            nums.pop(i)
            i -= 1
        else:
            i += 1

    nums = ''.join(map(str, nums))
    print(f'#{t} {nums}')