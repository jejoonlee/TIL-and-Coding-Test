import sys
sys.stdin = open('input.txt', 'r')

# 정점이랑 촌수도 같이 추가한다. 튜플의 형태로
# 예 (7, 0) 으로 시작해서 뒤의 0을 1씩 더하기

# N = 촌수
N = int(input())

visited = [False] * (N + 1)

# 촌수를 계산할 두 사람
per_1, per_2 = map(int, input().split())

# M = 관계의 개수
M = int(input())

links = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    links[v1].append(v2)
    links[v2].append(v1)

print(links)