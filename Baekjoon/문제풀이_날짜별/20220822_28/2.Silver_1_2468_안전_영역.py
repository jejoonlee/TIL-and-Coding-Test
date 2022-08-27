import sys
sys.stdin = open('input.txt')

# 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
# 델타 탐색 위, 아래, 오른쪽, 왼쪽
# 안전한 영역의 최대 개수를 계산

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

N = int(input())

terrain = [list(map(int, input().split())) for _ in range(N)]


# 높이는 1이상 100이하 정수 (안전지역이 0개이면 끝) min, max 구하기

min_height = min(list(map(int, min(terrain))))
max_height = max(list(map(int, max(terrain))))


safe = []
for rain in range(min_height, max_height + 1):
    # 안전 지대 개수 세는 것
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):

            # 지형이 비가 내린만큼 높으면 안전지대라고 설정
            # 그리고 순회를 안 한 곳을 탐색한다 (시간? 절약)
            if terrain[r][c] >= rain and visited[r][c] == False:
                cnt += 1
                visited[r][c] = True
                stack = [(r, c)]

                while len(stack) != 0:
                    cur_1, cur_2 = stack.pop()

                    for i in range(4):
                        sr = cur_1 + dr[i]
                        sc = cur_2 + dc[i]

                        if 0 <= sr < N and 0 <= sc < N:
                            if terrain[sr][sc] >= rain and visited[sr][sc] == False:
                                stack.append((sr, sc))
                                visited[sr][sc] = True
    
    # 안전 지대의 개수를 safe 리스트에 저장한다
    safe.append(cnt)


print(max(safe))