import sys
sys.stdin = open('input.txt', 'r')

def pprint(lst):
    for row in lst:
        print(row)


# 델타 탐색
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

island_count = 0

while True:
    island_count = 0

    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 지도 만들기
    map_ = [list(map(int, input().split())) for _ in range(m)]


    for r in range(m):
        for c in range(n):
            
            # dfs
            if map_[r][c] == 1:
                stack = [(r, c)]
                map_[r][c] = 'I'

                island_count += 1

                while len(stack) != 0:
                    r_1, c_1 = stack.pop()

                    for i in range(8):
                        sr = dr[i] + r_1
                        sc = dc[i] + c_1

                        if 0 <= sr < m and 0 <= sc < n:
                            if map_[sr][sc] == 1:
                                stack.append((sr, sc))
                                map_[sr][sc] = 'I'
    print(island_count)