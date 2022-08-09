# 그래프 입력이 주어질 때 유방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
# 둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

import sys
sys.stdin = open('유방향_input.txt', 'r')

def pprint(lst):
    for i in lst:
        print(i)

# N 정점의 개수, M 간선의 개수
# u 시작점, v 끝점

N, M = map(int, input().split())

# N에 +1 을 하는 것은, 1부터 시작함
# 인덱스는 0부터 시작하는게 기본
matrix = [[0] * (N + 1) for _ in range(N + 1)]
ad_lst = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    # 시작점과 끝의 점의 입력

    matrix[u][v] = 1

    ad_lst[u].append(v)

pprint(matrix)
print(ad_lst)
