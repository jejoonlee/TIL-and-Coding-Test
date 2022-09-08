import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for _ in range(T):
    command = input()
    N = int(input())
    array = input()
    flag = True

    # ','로 split 되어 있는 것을 리스트 안에 넣는다
    array = deque(array[1:-1].split(','))

    for c in command:
        queue = []
        if c == 'R':
            while len(array) != 0:
                queue.append(array.pop())
            for i in queue:
                array.append(i)
        
        elif c == 'D':
            if array:
                array.popleft()
            else:
                flag = False
                print('error')

    if flag != False:
        array = list(map(int, array))
        print(array)