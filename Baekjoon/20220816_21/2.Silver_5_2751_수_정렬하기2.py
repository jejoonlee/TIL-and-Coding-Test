import sys
sys.stdin = open('input.txt')

# 오름차순으로 정렬하기

N = int(input())

nums = []
for n in range(N):
    num = int(input())
    nums.append(num)

nums.sort()

for number in nums:
    print(number)