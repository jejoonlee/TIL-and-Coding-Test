import sys
sys.stdin = open('input.txt')

from bisect import bisect_left, bisect_right

N = int(input())
my_card = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

my_card.sort()

result = []

for i in card:
    if i == my_card[bisect_left(my_card, i)]:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))