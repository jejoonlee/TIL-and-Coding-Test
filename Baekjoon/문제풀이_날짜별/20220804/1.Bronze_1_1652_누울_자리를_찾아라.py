
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

room = [list(input()) for _ in range(N)]
# 입력값의 개수와 N의 숫자에 따라 행렬이 만들어진다

# # 열과 행에 누울 수 있는 공간의 결과를 result에 넣어준다
# result = [0, 0]
# # 정사각형이기 때문에 똑같이 써도 됨
# for i in range(N):
#     row, column = 0, 0
#     for j in range(N):
#         if room[i][j] == '.': # 열 먼저
#             row += 1
#         else:
#             row = 0
#         if row == 2:    # 2개 연속으로 공간이 있으면
#             result[0] += 1  # result에 바로 1을 누적시키기
        
#         if room[j][i] == '.':
#             column += 1
#         else:
#             column = 0
#         if column == 2:
#             result[1] += 1

# print(*result)



r_result = []
for i in range(len(room)):
    space = 0
    row = []
    for j in range(N):
        if room[i][j] == '.':
            space += 1
        else:
            row.append(space)
            space = 0
    row.append(space)
    r_result.append(max(row))

c_result = []
for i in range(N):
    space = 0
    column = []
    for j in range(len(room)):
        if room[j][i] == '.':
            space += 1
        else:
            column.append(space)
            space = 0
    column.append(space)
    c_result.append(max(column))



r_final = 0
for i in r_result:
    if i > 1:
        r_final += 1

c_final = 0
for i in c_result:
    if i > 1:
        c_final += 1

print(r_final, c_final)
