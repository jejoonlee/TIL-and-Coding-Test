
import sys
sys.stdin = open('input.txt', 'r')

ball = [1, 0, 0]

N = int(input())

for n in range(N):
    x, y = map(int, input().split())
    ball[x - 1], ball[y - 1] = ball[y - 1], ball[x - 1]
    print(ball)

for i in range(len(ball)):
    if ball[i] == 1:
        print(i + 1)