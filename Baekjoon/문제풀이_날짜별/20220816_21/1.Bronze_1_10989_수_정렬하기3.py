
import sys
sys.stdin = open('input.txt')

# 시간 초과

# T = int(input())

# num_ord = []
# for t in range(T):
#     num = int(sys.stdin.readline())
#     num_ord.append(num)

# num_ord.sort()

# for i in num_ord:
#     print(i)


# 정렬 / append를 안 하고 수를 가지고 오기
# 10000 보다 작거나 같은 자연수
# 인덱스는 0부터 시작하니깐 10000에 1을 더해야 한다

import sys

T = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(T):
    a = int(sys.stdin.readline())
    arr[a] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)