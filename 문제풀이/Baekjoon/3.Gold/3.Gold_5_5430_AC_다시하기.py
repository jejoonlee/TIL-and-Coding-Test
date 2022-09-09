import sys
sys.stdin = open('input.txt')

# R : 배열 뒤집기
# D : 배열에 있는 제일 앞에 숫자 버리기
# 단 D를 호출했는데, 배열에 아무것도 없으면 error
# 호출이 다 끝났는데 배열에 아무것도 없으면 []

# 중요한 것! 한번 할때마다 배열을 뒤집으면 시간이 많이 걸린다
# 뒤집어서 첫 번째 숫자를 빼거나, 뒤집지 않은 상태에서 맨 뒤의 숫자를 빼는 것은 똑같다
# 단 마지막에 출력하기 전에 배열을 잘 만드는 것이 중요

# 즉 홀수이면 배열이 뒤집혀야 되는 것이고, 짝수면 그대로 있는다

from collections import deque

T = int(input())

for _ in range(T):
    # 수행할 함수
    p = input()
    # 배열에 들어가 있는 수의 개수
    n = int(input())
    # 배열에 들어가 있는 수들
    queue = deque(input()[1:-1].split(','))
    flag = True
    # R이 나올때마다 1씩 누적한다
    # 짝수이면 배열이 그대로이고
    # 홀수이면 배열이 뒤집혀있는 것
    cnt = 0

    # 처음부터 배열에 아무것도 없을 시에는 error
    # 이 조건을 안 넣을 시, queue안에 '' 가 들어가서, 배열에 요소가
    # 있다고 판단한다
    if n == 0:
        queue = []
    
    for command in p:
        if command == 'R':
            cnt += 1
        
        elif command == 'D':
            if len(queue) != 0:
                if cnt % 2 == 1:
                    queue.pop()

                elif cnt % 2 == 0:
                    queue.popleft()
            else:
                flag = False
                print('error')
                break
    
    if flag == True:
        if cnt % 2 == 1:
            queue.reverse()
            queue = ','.join(queue)
            print(f'[{queue}]')

        else:
            queue = ','.join(queue)
            print(f'[{queue}]')