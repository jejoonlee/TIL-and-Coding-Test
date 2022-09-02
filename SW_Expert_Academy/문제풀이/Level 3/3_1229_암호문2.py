import sys
sys.stdin = open('input.txt')

# l, x, y, s : 삽입문 x의 위치에 y개의 숫자(s)들을 넣어라
# d, x, y : 삭제문, x위치 바로 다음부터 y개의 숫자를 삭제한다

for t in range(10):

    # 암호문의 길이
    N = int(input())
    # 암호문
    password = list(input().split())
    # 명령어의 개수
    C = int(input())
    # 명령어
    commend = list(input().split())

    while len(commend) != 0:
        com = commend.pop(0)

        # 명령어가 I 면 암호문의 위치 (x)와 y를 명령문에서 꺼내서, x,y 로 저장한다
        # 그리고 y개 만큼 명령문에서 꺼내서 암호문 x에 넣는다
        # 단 y 반대로 순회를 해야한다
        if com == 'I':
            x = int(commend.pop(0))
            y = int(commend.pop(0))
            for i in range(y)[::-1]:
                s = commend.pop(i)
                password.insert(x, s)

        # 명령문이 D로 시작하면, y만큼 순회하면서, 암호문 x번째에 위치한 숫자를 빼준다
        if com == 'D':
            x = int(commend.pop(0))
            y = int(commend.pop(0))
            for j in range(y):
                password.remove(password[x])
        
    password = ' '.join(password[0:10])
    print(f'#{t+1} {password}')