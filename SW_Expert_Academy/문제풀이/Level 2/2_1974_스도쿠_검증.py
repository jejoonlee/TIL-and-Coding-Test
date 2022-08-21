
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    small_sudoku = [[False] * 9 for _ in range(9)]

    dr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dc = [0, 1, 2, 0, 1, 2, 0, 1, 2]

    flag = True
    column = []

    for r in range(9):
        for c in range(9):

            # row에서 숫자가 겹치지 않는지 확인
            if flag == True:
                row_cnt = sudoku[r].count(sudoku[r][c])

                if row_cnt != 1:
                    flag = False
                    break
                
            if flag == True:
                column.append(sudoku[c][r])

                # column에서 겹치지 않는지 확인
                if len(column) == 9:
                    for i in column:
                        column_cnt = column.count(i)
                        
                        if column_cnt != 1:
                            flag = False
                            break                    
                    column = []
            
            if flag == True:
                if small_sudoku[r][c] == False:
                    small_cnt = []
                    for j in range(9):
                        sr = r + dr[j]
                        sc = c + dc[j]

                        if 0 <= sr < 9 and 0 <= sc < 9 and small_sudoku[sr][sc] == False:
                            small_cnt.append(sudoku[sr][sc])
                            small_sudoku[sr][sc] = True
                    
                    for k in range(9):
                        small_count = small_cnt.count(small_cnt[k])
                        if small_count != 1:
                            flag = False
                            break

    if flag == False:
        print(f'#{t} 0')
    else:
        print(f'#{t} 1')