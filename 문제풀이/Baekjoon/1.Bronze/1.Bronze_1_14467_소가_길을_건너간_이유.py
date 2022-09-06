import sys
sys.stdin = open('input.txt', 'r')

# N = 관찰 횟수

N = int(input())

cow_locate = {}

# 소의 움직임
cnt = 0

for _ in range(N):
    c, m = map(int, input().split())

    if c not in cow_locate:
        cow_locate[c] = m
        
    elif c in cow_locate and cow_locate[c] != m:
        cow_locate[c] = m
        cnt +=1

print(cnt)