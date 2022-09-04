
# 주어진 N 길이의 숫자열을 오름차순으로 정렬
import sys
sys.stdin = open('input.txt')

# array를 만들고 array list의 인덱스에 주어진 숫자를 넣는다
# array는 주어진 입력 값들 중에 제일 높은 값을 1을 더한다
# 그리고 앞에서부터 하나씩 가져오기

T = int(input())

for t in range(1, T + 1):

    N = int(input())

    nums = list(map(int, input().split()))

    arr = [0] * (max(nums) + 1)
    result = []

    # 인덱스를 기준으로 인덱스 값에 1씩 누적
    for num in nums:
        arr[num] += 1
    
    # 누적된 인덱스 값을 하나씩 빼면서
    # 인덱스를 result 리스트에 넣는다
    for i in range(len(arr)):
        if arr[i] != 0:
            while arr[i] != 0:
                result.append(i)
                arr[i] -= 1

    result = ' '.join(map(str, result))
    print(f'#{t} {result}')