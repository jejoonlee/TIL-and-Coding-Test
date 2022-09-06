
# push X: 정수 X를 큐에 넣는다
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
        # 큐에 정수가 없으면 -1을 출력
# size: 큐에 들어있는 정수의 개수를 출력
# empty: 큐가 비어있으면 1, 아니면 0을 출력
# front: 큐의 가장 앞에 있는 정수를 출력. 정수가 없으면 -1 출력
# back: 큐의 가장 뒤에 있는 정수를 출력. 없으면 -1 출력

import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())

# 리스트를 deque로 만들어 queue를 만들었다
# leftpop을 사용하기 위해
lst = []
queue = deque(lst)

for _ in range(N):
    num = sys.stdin.readline().split()
    
    # 명령어가 'push'면 뒤에 있는 정수를 큐에 넣기
    if num[0] == 'push':
        queue.append(num[1])

    # 큐에 정수가 있으면 첫번째 정수를 출력하고 pop한다
    # 없으면 -1 출력
    elif num[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)

    # size는 큐 안에 있는 정수들의 개수를 출력
    elif num[0] == 'size':
        print(len(queue))

    # empty는 큐 안에 정수가 있는지 없는지의 여부를 출력
    elif num[0] =='empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # front는 앞에 숫자를 출력하는 것
    # 없으면 -1
    elif num[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    # back은 큐의 제일 마지막 숫자를 출력
    # 없으면 -1
    elif num[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])