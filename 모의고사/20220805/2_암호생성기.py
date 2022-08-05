import sys

sys.stdin = open("_암호생성기.txt")

from collections import deque

for t in range(10):
    T = int(input())       
    nums = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        num_add = nums[0] - cnt
        if num_add > 0:
            nums.append(num_add)
            cnt += 1
            nums.popleft()
            # 1 사이클이 1부터 5를 빼는 것이니깐
            # cnt가 6이 되면 1로 초기화 시킨다
            if cnt == 6:
                cnt = 1
        elif num_add <= 0:
            nums.append(0)
            nums.popleft()
            break

    result = ' '.join(list(map(str, nums)))

    print(f'#{T} {result}')
