import sys
sys.stdin=open('input.txt')

# N : 문서의 개수
# M : 몇 번째로 인쇄되었는지 궁금한 문서

from collections import deque

t = int(input())

for _ in range(t):
    N, M = map(int, input().split())

    nums = deque(list(map(int, input().split())))
    index = deque([0]*N)
    index[M] = 'A'
    cnt = 0

    num_ord = sorted(nums)

    while True:
        # index에 A를 발견하고, 우선순위일 경우, cnt에 1을 누적하고
        # while문을 끝내기
        if nums[0] == num_ord[-1] and index[0] == 'A':
            cnt += 1
            break

        # 우선순위일 경우, 리스트에서 빼기
        # 그리고 cnt에 1을 누적
        elif num_ord[-1] == nums[0]:
            num_ord.pop()
            nums.popleft()
            index.popleft()
            cnt += 1
        
        # 순회하면서 우선순위가 아닐 경우,
        # 리스트 제일 뒤로 보내기
        else:
            a = nums.popleft()
            b = index.popleft()
            nums.append(a)
            index.append(b)

    print(cnt)