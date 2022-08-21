import sys
sys.stdin = open('input.txt', 'r')

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
                if not visited[c]:
                    # True로 바꿔주고
                    visited[c] = True
                    # 스택에 넣는다
                    stack.append(c)

print(cnt)