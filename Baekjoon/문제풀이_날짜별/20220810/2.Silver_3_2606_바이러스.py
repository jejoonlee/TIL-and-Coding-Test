import sys
sys.stdin = open('input.txt', 'r')


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