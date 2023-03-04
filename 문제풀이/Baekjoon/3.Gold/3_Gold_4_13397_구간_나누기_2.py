import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
array = list(map(int, input().split()))

def groups(mid):
    
    min_num, max_num = array[0], array[0]
    count = 1

    for i in range(N):
        min_num = min(min_num, array[i])
        max_num = max(max_num, array[i])

        if max_num - min_num > mid:
            count += 1
            min_num, max_num = array[i], array[i]

    return count


left, right = 0, max(array)
result = max(array)

while left <= right:
    mid = (left + right) // 2
    
    group_num = groups(mid)

    if group_num <= M:
        right = mid - 1
        result = min(result, mid)

    else:
        left = mid + 1

    print(result)

print(result)