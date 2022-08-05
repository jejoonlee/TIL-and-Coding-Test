import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int(input().split()))
    # N에서 인덱스는 0부터 시작
    M = M - 1

    area = [list(map(int, input().split())) for _ in range(N)]
    
    