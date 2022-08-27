import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 똑바로 읽어도 거꾸로 읽어도 똑같은 문장을 '회문'이라고 함
# 가로 세로만
# 슬라이싱으로 

for t in range(1, 11):
    num = int(input())
    matrix = [list(input()) for _ in range(8)]

    cnt = 0
    for r in range(8):
        for c in range(8):
            
            # row에서 회문을 구하는 것
            if c + num <= 8: 
                h_word = matrix[r][c : c + num]

                if h_word == h_word[::-1]:
                    cnt += 1

            # column에서 회문을 구하는 것
            if r + num <= 8:
                word = ''
                for k in range(num):
                    word += matrix[r + k][c]

                if word == word[::-1]:
                    cnt += 1
                                    
    print(f'#{t} {cnt}')