# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

import sys
sys.stdin = open('무방향_input.txt', 'r')

def pprint(lst):
    for row in lst:
        print(row)

# n = 노드의 개수
# m = 간선의 개수
n, m = map(int,input().split())

matrix = [[0] * (n  + 1) for _ in range(n + 1)]

ad_list = [[] for _ in range(n + 1)]

for i in range(m): # 간선의 개수
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

    ad_list[u].append(v)
    ad_list[v].append(u)

pprint(matrix)


print(ad_list)