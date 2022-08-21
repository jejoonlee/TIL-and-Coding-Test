import sys
sys.stdin = open('input.txt')

# 델타 탐색

# 5개 연속으로 놓여진 색깔이 이기는 것
# 델타 탐색 후 똑같은 방향으로 연결된게 있는지 확인

# 단 6개 이상이면 이긴 것이 아님
# 기준점에서 그 전 점을 확인/ 마지막 점에서 그 다음 점을 확인

area = [list(map(int, input().split())) for _ in range(19)]

dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

Flag = False

for r in range(19):
    for c in range(19):

        if area[r][c] == 1 or area[r][c] == 2:

            for i in range(4):
                cnt = 1

                sr = r + dr[i]
                sc = c + dc[i]
                
                # 탐색 중 값이 똑같은 방향이 나오면 그 방향으로 탐색을 시작
                while (0 <= sr < 19 and 0 <= sc < 19) and area[r][c] == area[sr][sc]:

                    # 그리고 연속된 수로 cnt에 1을 누적시키기
                    cnt += 1
                    # 똑같은 방향을 탐색 
                    sr = sr + dr[i]
                    sc = sc + dc[i]

                if cnt == 5:
                    # 기준점에서 뒤에 점의 값을 확인 하는 것
                    br = r - dr[i]
                    bc = c - dc[i]

                    if not(0 <= br < 19 and 0 <= bc < 19) or area[r][c] != area[br][bc]:
                        print(area[r][c])
                        print(r + 1, c + 1)
                        
                        Flag = True


if Flag == False:
    print(0)