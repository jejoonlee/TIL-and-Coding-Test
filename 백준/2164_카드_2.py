import sys
from collections import deque

input = sys.stdin.readline

cards = deque(range(1, int(input()) + 1))

if len(cards) == 1:
    print(1)

else:
    while True:

        cards.popleft()

        if len(cards) == 1:
            break

        cards.append(cards.popleft())

    print(cards[0])
