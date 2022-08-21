# ✍️ 문제풀이

[후기](#후기)

[1063](#1063-킹)

[4963 섬의 개수](#4963-섬의-개수)



## 백준 풀이



### 1063 킹

```python
def pprint(lst):
    for row in lst:
        print(row)

# 킹 하나, 돌 하나가 있다

k, s, m = input().split()
m = int(m)

dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]
command = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

chess_board = [[0] * 8 for _ in range(8)]

# k와 s의 위치를 행열로 표시
k_row, k_column = 8 - int(k[1]), ord(k[0]) - 65
s_row, s_column = 8 - int(s[1]), ord(s[0]) - 65

# 1은 킹의 위치 / 2는 돌의 위치
chess_board[k_row][k_column] = 1
chess_board[s_row][s_column] = 2


for com in range(m):
    com = input()

    # command에서 com에서 입력한 같은 값의 인덱스를 가지고 온다
    move = command.index(com)

    kr = k_row + dr[move]
    kc = k_column + dc[move]

    sr = s_row + dr[move]
    sc = s_column + dc[move]
    
    # king이 움직일 수 있는 조건은, 킹이 범위 안에 있을 때
    if (0 <= kr < 8 and 0 <= kc < 8):

        if chess_board[kr][kc] == chess_board[s_row][s_column]:
            # 돌을 움직였을 때 범위 밖으로 안 나가면, if문을 실행
            if 0 <= sr < 8 and 0 <= sc < 8:
                # 움직인 후에 s_row와 s_column의 위치를 갱신해준다
                chess_board[s_row][s_column] = 0
                chess_board[sr][sc] = 2
                s_row, s_column = sr, sc

                # 움직인 후에 k_row와 k_column의 위치를 갱신해준다
                chess_board[k_row][k_column] = 0
                chess_board[kr][kc] = 1
                k_row, k_column = kr, kc
        else:
            chess_board[k_row][k_column] = 0
            chess_board[kr][kc] = 1
            k_row, k_column = kr, kc


k_column, k_row = chr(k_column + 65), 8 - k_row

s_column, s_row = chr(s_column + 65), 8 - s_row

print(k_column, k_row, sep = '')
print(s_column, s_row, sep='')
```

- 델타 탐색처럼, 값을 한번에 가지고 올 수 있도록, 같은 위치에 인덱스에 필요한 값을 리스트에 넣는다



### 4963 섬의 개수

```python
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
```

