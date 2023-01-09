import sys
sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    N = int(input())
    rank = []
    
    for n in range(N):
        rank.append(tuple(map(int, input().split())))
    
    rank.sort()
    cnt = 1
    score = rank[0][1]

    for r in range(1, len(rank)):
        if rank[r][1] < score:
            cnt += 1 
            score = rank[r][1]

    print(cnt)