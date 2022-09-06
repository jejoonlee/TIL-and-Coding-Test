from pprint import pprint

# import sys
# sys.stdin = open('input.txt', 'r')

# N, M = map(int, input().split())

# castle = [list(input()) for _ in range(N)]

# # 각 행과 열에 X가 존재하면 X를 1로 바꿔준다
# # 그리고 각각 행과 열에 있는 1들을 더했는데, 0이 나오면
# # 각각 행과 열에 1씩 더해준다.
# # 그 행과 열의 값 중 제일 큰 값이 답이다

# column = [0] * M
# row = [0] * N

# for i in range(len(castle)):
#     for j in range(len(castle)):
#         if castle[i][j] == 'X':
#             row[i] = 1
#             column[j] = 1

# col_cnt = 0
# row_cnt = 0

# for i in row:
#     if i == 0:
#         row_cnt += 1

# for j in column:
#     if i == 0:
#         col_cnt += 1

# print(max(row_cnt, col_cnt))


N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

row = 0
for i in range(N):
# i는 열 'N'의 인덱스
    if 'X' not in castle[i]:
    # 열에 X가 없으면 1씩 더해주기
        row += 1

column = 0
for j in range(M):
# j가 기준점이 되는 것
# 2중 for문
    if 'X' not in [castle[i][j] for i in range(N)]:
        column += 1

print(max(row, column))

# for j in range(M):
#     for i in range(N):
#         print(j, i)