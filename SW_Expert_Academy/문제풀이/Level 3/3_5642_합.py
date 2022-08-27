import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    M = list(map(int, input().split()))

    
    # visited = [False] * N

    # num = M[0]
    # for i in range(N):
    #     for j in range(N):
    #         if visited[j] == False:
    #             total = sum(M[i:j + 1])
    #             if total > num:
    #                 num = total
    #     visited[i] = True
    
    print(f'#{t} {num}')
