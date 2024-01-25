from collections import deque

N, B = map(int, input().split(' '))

answer = deque()

while N > 0:

    temp = N % B
    N //= B

    if temp > 9:
        temp = chr(temp + 55)
    temp = str(temp)

    answer.appendleft(temp)

print(''.join(answer))