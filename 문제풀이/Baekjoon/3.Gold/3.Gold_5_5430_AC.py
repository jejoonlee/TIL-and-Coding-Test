import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    array = input().rstrip()[1:-1].split(',')
    cnt = 0
    flag = True

    queue = deque(array)

    if n == 0:
        queue = []

    for command in p:
        # 뒤집어지는 기준은 홀수는 배열이 뒤집어 지고
        # 짝수는 기존 배열이랑 똑같다
        if command == 'R':
            if queue:
                cnt += 1
        
        elif command == 'D':
            # array에 숫자가 있으면
            if queue:
                # 뒤집어져 있을 때에는 맨 뒤에 있는 숫자를 pop한다
                if cnt % 2 == 1:
                    queue.pop()
                
                # 원상태이면 맨 앞의 숫자를 pop한다
                elif cnt % 2 == 0:
                    queue.popleft()
            
            else:
                print('error')
                flag = False
                break
    
    if flag == True:
        if cnt % 2 == 1:
            queue.reverse()
            queue = ','.join(queue)
            print(f'[{queue}]')
        else:
            queue = ','.join(queue)
            print(f'[{queue}]')