import sys
sys.stdin = open('input.txt', 'r')


# 아래 빈 공간이 없어질 때까지 내리기 
# 조건 (while문)
# 1. 현재 박스 아래에 박스가 없어야 한다
#       현재 박스 아래에 박스가 없으면, 1칸 내려가고, 내려간 만큼 1씩 누적한다
# 2. 박스는 바닥을 벗어나면 안된다. --> 리스트 범위를 벗어나면 안 된다
# 밑에서 위로 

# reversed 함수 (뒤에서 앞으로 순회, 반대로 순회)

# and와 or 조건이 있을 때에, 앞에 있는 조건부터 본다

def pprint(command):
    for row in command:
        print(row)


# N, M = map(int, input().split())

# matrix = [list(map(int, input().split())) for _ in range(N)]

# cnt = 0
# for i in range(M):
#     for j in range(N - 1, -1, -1):
#         if matrix[j][i] == 1:
#         # 만약 박스가 있을 시
#             while True:
#                 if j + 1 == N:
#                 # 박스 밑이 범위 밖이면, 위에 공간으로 올라가라
#                     break
#                 if matrix[j + 1][i] == 1:
#                 # 박스 밑에, 박스가 있다면 위에 공간으로 올라가라
#                     break
        
#         # 두 조건이 모두 거짓일 때,
#         # 박스를 공간 한칸 아래로 내려놓고,
#         # 지금 공간에는 0을 넣어준다
#                 matrix[j + 1][i] = 1
#                 matrix[j][i] = 0
#                 j += 1
#         # 밑에 공간이 없을 때 까지 한다
#                 cnt += 1

# pprint(matrix)
# print(cnt)

T = int(input())

for t in range(T):
# 열고 행 입력 받기
    N, M = map(int, input().split())

    # 행열 만들기
    area = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 1. 행을 기준으로 순회하기 (밑에서 위로)
    for x in range(M):
        for y in range(N - 1, -1, -1):
    # 상자가 발견될 경우 밑에 공간이 없어질 때까지 밑으로 보냄
            if area[y][x] == 1:
                while True:
            # 리스트 밖으로 나가면 안 됨           
                        if y + 1 == N:
                            break
                        elif area[y + 1][x] == 0:
                            area[y][x] = 0
                            area[y + 1][x] = 1
                            cnt += 1
                        y += 1
                        # 이게 없으면 if와 elif문이 무한 반복
                        # y를 1씩 더해줘서 break를 하게 만들어야 한다
                        # 즉 1 밑에 0이 있으면, 1을 0밑으로 계속 보내되
                        # 1 밑에도 1이 있으면 y가 1씩 커져서, 
                        # if문의 조건과 만족하게 된다
    print(cnt)

