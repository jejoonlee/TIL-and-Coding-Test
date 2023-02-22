import sys

sys.stdin = open("input.txt")

N = int(input())
array = list(map(int, input().split()))
budget = int(input())

array.sort()

left, right = 0, array[-1]

if sum(array) <= budget:
    print(max(array))

else:
    result = 0
    while left <= right:
        mid = (left + right) // 2
        temp = 0

        for num in array:
            temp += min(num, mid)

        if temp <= budget:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    print(result)
