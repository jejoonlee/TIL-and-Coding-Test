
import sys
sys.stdin = open('input.txt', 'r')

R, C = map(int, input().split())

parking = [list(input()) for _ in range(R)]

dr = [1, 1, 0]
dc = [0, 1, 1]

destroy = [0, 0, 0, 0, 0]
empty = '.'
car = 'X'
building = '#'

for x in range(R):
    for y in range(C):
        flag = True
        cnt = 0

        # 만약 해당 좌표에 건물이 있으면 아무것도 할 수 없다
        if parking[x][y] == building:
            continue

        if parking[x][y] == car:
            cnt += 1
            
            # 델타 탐색
        for i in range(3):
            sr = dr[i] + x
            sc = dc[i] + y

            if 0 <= sr < R and 0 <= sc < C:

                if parking[sr][sc] == building:
                    flag = False
                    break

                elif parking[sr][sc] == car:
                    cnt += 1
            
            else:
                flag = False

            
        if flag == True:
            destroy[cnt] += 1

for i in destroy:
    print(i)
                



                
        # cnt = 0
        # # 차를 하나도 안 부수고 주차할 수 있는 공간
        # if parking[x][y] == empty:

        #     # 델타 탐색하기
        #     for i in range(3):
        #         sr = dr[i] + x
        #         sc = dc[i] + y

        #         if 0 <= sr < R and 0 <= sc < C:
        #             if parking[sr][sc] == empty:
        #                 cnt += 1
        #                 if cnt == 3:
        #                     park += 1

# car를 리스트를 넣어서
# 인덱스로 풀면 된다

# 차 0대, 차 1대, 차 2대, 차 3대, 차 4대
# [0, 0, 0, 0, 0]

