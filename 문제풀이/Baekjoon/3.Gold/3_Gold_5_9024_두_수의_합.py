import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()

    count = 0


    while count == 0:
        left, right = 0, len(array) - 1

        while left < right:
            if array[left] + array[right] < K:
                left += 1
            
            elif array[left] + array[right] > K:
                right -= 1

            else:
                count += 1
                left += 1
            
        K += 1


    print(count)