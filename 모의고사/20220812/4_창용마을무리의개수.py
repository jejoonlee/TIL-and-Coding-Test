import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for t in range(1, T + 1):
    # N = 사람의 수 / M = 간선
    N, M = map(int, input().split())

    rel = [[] for _ in range(N)]
    know = [False] * (N)

    for _ in range(M):
        v1, v2 = map(int, input().split())

        # 관계의 수만 나타내면 되니깐,
        # 원래 인덱스를 활용하는게 더 쉽다 (개인적)
        v1 = v1 - 1
        v2 = v2 - 1
        rel[v1].append(v2)
        rel[v2].append(v1)

    cnt = 0
    for i in range(len(know)):
        if know[i] == False:
            stack = [i]
            know[i] = True

            cnt += 1

            while len(stack) != 0:
                current = stack.pop()

                for cur in rel[current]:
                    if not know[cur]:
                        know[cur] = True
                        stack.append(cur)
    
    print(f'#{t} {cnt}')