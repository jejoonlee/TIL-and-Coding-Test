import sys
sys.stdin = open('input.txt')

N = int(input())
array = list(map(int, input().split()))

array.sort()

left = 0
right = N - 1

current_min = abs(array[left] + array[right])
left_ans, right_ans = array[left], array[right]
min_num = []

while left < right:
    temp = array[left] + array[right]

    if abs(temp) < current_min:
        current_min = abs(temp)
        left_ans, right_ans = array[left], array[right]

        if temp == 0:
            break
    
    if temp > 0:
        right -= 1
    
    else:
        left += 1

print(left_ans, right_ans)