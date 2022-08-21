import sys
sys.stdin = open('input.txt')

# 전체 사람의 수
n = int(input())

# 서로 다른 두 사람들의 번호
per_1, per_2 = map(int, input().split())

#관계 개수
m = int(input())

# 관계 인접 리스트
relation = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    relation[v1].append(v2)
    relation[v2].append(v1)

# 아는 관계
know = [False] * (n + 1)

# dfs 만들기

stack = [(per_1, 0)]
know[per_1] = True

while len(stack) != 0:
    current, count = stack.pop()

    if current == per_2:
        break
    
    for cur in relation[current]:
        if know[cur] == False:
            know[cur] = True
            stack.append((cur, count + 1))
    

if know[per_2] == True:
    print(count)
else:
    print(-1)