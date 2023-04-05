import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

nums = []

def backtracking(start):

    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return
    
    for num in range(start, N + 1):
        if num not in nums:
            nums.append(num)
            backtracking(num + 1)
            nums.pop()

backtracking(1)
