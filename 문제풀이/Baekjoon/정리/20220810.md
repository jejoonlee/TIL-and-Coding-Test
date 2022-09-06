# ✍️ 문제풀이

[후기](#후기)

[2606 바이러스](#2606-바이러스)

[11724 연결 요소의 개수](#11724-연결-요소의-개수)



## 백준 풀이



### 2606 바이러스

```python
com = int(input())
link = int(input())

com_lst = [False] * (com + 1)

com_links = [[] for _ in range(com + 1)]

for _ in range(link):
    v1, v2 = map(int, input().split())
    com_links[v1].append(v2)
    com_links[v2].append(v1)


# 1. 시작점을 stack에 넣어준다
# 2. stack에 넣은 시작점을 하나씩 빼준고, index로 만든다
# 3. index 안에 있는 값들을 가지고 와서 False면 True로 변환한다
# 4. 그 값들을 stack에 넣어주고, stack이 없어질때까지 진행한다

def dfs(start):
    stack = [start]
    # 스택에 start를 넣어주고
    com_lst[start] = True
    # start를 인덱스로 가지고 와서 com_lst에 False를 True로 바꿔준다

    while len(stack) != 0:
        current = stack.pop()

        for c in com_links[current]:
            if com_lst[c] == False:
                com_lst[c] = True
                stack.append(c)
    
    return sum(com_lst) - 1
    # 컴퓨터 1을 빼고, 바이러스 걸린 컴퓨터 수

print(dfs(1))
```





### 11724 연결 요소의 개수

```python
# N = 정점의 개수 / M = 간선의 개수

N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u = u - 1
    v = v - 1
    adj[u].append(v)
    adj[v].append(u)
    # 인덱스는 0부터 시작해서, 시작점을 0으로 맞춰준다
    # 즉 모든 원소에 1을 뺀다

visited = [False] * (N)

# 연결 요소를 카운트 하기
cnt = 0

# 어차피 시작점은 0 이다
# 그리고 visited 모든 값들이 True일 때, 그만 한다
for i in range(len(visited)):
    if visited[i] == False:
        #시작점을 스텍에 넣은다
        stack = [i]
        visited[i] = True

        # while문 시작하기 전에 연결 요소에 1을 누적시킨다
        # 만약 연결 요소가 2개면 어차피 또 for문으로 온다
        cnt += 1

        while len(stack) != 0: 
            # 스텍에 있는 값들을 뺀다
            current = stack.pop()

            # adj에 있는 current번째의 값을 가지고 온다
            for c in adj[current]:
                # 숫자에 방문을 안 한 상태면
                if visited[c] == False:
                    # True로 바꿔주고
                    visited[c] = True
                    # 스택에 넣는다
                    stack.append(c)

print(cnt)
```

