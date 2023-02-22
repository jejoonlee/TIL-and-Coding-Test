import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result = 0

for i in range(N):

    new_array = numbers[:i] + numbers[i + 1:]

    left, right = 0, len(new_array) - 1

    while left < right:
        add_num = new_array[left] + new_array[right]
        
        if add_num == numbers[i]:
            result +=1
            break
        
        elif add_num > numbers[i]:
            right -= 1
        
        elif add_num < numbers[i]:
            left += 1

print(result)