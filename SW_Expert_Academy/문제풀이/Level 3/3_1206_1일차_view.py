import sys
sys.stdin = open('input.txt')

# 빌딩 앞 뒤로 두 칸씩의 기준으로 비교를 해야 함
# 앞 뒤로 두 칸에 현재 빌딩보다 높은 빌딩이 없으면, 현재 빌딩에서 4빌딩 중
# 제일 높은 빌딩의 차이를 구하면 조망권이 확보된 세대 수를 구할 수 있음

for t in range(1, 11):

    N = int(input())
    b = list(map(int, input().split()))
    
    # view는 조망권이 확보된 세대 수를 저장한 값
    view = 0
    
    # 리스트 시작하고 2칸과 마지막 2칸은 모두 0이다
    for i in range(2, len(b) - 2):

        # 앞 뒤 2칸씩, 총 4칸 중 제일 높은 빌딩
        max_view = 0

        # i 기준으로 i 앞에 2 빌딩과, 뒤에 2 빌딩을 비교하는 것
        # 모두 i 보다 낮아야 조건문 성사
        if b[i -2] < b[i] and b[i - 1] < b[i] and b[i] > b[i + 1] and b[i] > b[i + 2]:
            # b[i-2], b[i-1], b[i+1], b[i+2] 중 제일 높은 빌딩
            max_view = max(b[i-2], b[i-1], b[i+1], b[i+2])
            view += b[i] - max_view
        
    print(f'#{t} {view}')