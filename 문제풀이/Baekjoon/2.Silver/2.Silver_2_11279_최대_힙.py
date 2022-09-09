import sys
sys.stdin = open('input.txt')

# 아무것도 없는 배열을 만든다
# 1. 배열에 자연수 x를 넣는다
# 2. 배열에서 가장 큰 값을 출력하고, 배열에서 제거한다

# N은 연산의 개수
# 이후의 정보는 x / x가 0이면 2번을 실행하는 것
# 만약 x가 0인데 배열이 비어 있는 경우는 0을 출력

import heapq

array = []
heapq.heapify(array)

N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(array) == 0:
            print(0)
        else:
            print(-heapq.heappop(array))
    else:        
        heapq.heappush(array, -x)