import sys
sys.stdin = open('input.txt')

# I, x, y, s : 암호문 x 위치에 y개만큼의 s라는 암호들을 넣는다 (단 y개를 반대로 순회)
# D, x, y : 암호문 x위치에 y개만큼 뺀다
# A, y, s: 암호문 맨 마지막에 y개만큼의 s라는 암호들을 넣는다 (맨 뒤라서 y개를 그냥 순회해도 된다)
# 여기서 리스트는 인덱스를 사용해서 x위치는 +1을 안 해도 된다

for t in range(10):
    # 원본 암호문의 길이
    N = int(input())
    # 암호문들
    password = list(input().split())
    # 명령어의 개수
    C = int(input())
    # 명령어
    commend = list(input().split())

    while len(commend) != 0:
        com = commend.pop(0)

        if com == 'I':
            x = int(commend.pop(0))
            y = int(commend.pop(0))
            # password의 x위치에 s(암호)를 insert를 통해 넣는다
            for i in range(y)[::-1]:
                s = commend.pop(i)
                password.insert(x, s)

        if com == 'D':
            x = int(commend.pop(0))
            y = int(commend.pop(0))
            # password[x] 값을 password에서 y만큼 꺼낸다
            for j in range(y):
                password.pop(x)

        if com == 'A':
            y = int(commend.pop(0))
            # y개만큼 password 맨 뒤에 s를 넣어라.
            for k in range(y):
                s = commend.pop(0)
                password.append(s)

    password = ' '.join(password[0:10])

    print(f'#{t + 1} {password}')