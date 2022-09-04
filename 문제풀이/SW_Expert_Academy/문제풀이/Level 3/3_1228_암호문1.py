import sys
sys.stdin = open('input.txt')

# l (암호문 시작) x, y, s
# 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입. s부터는 덧붙일 숫자.
# y는 주어진 원본 암호문의 인덱스

for t in range(10):
    # 원본 암호문의 길이
    N = int(input())
    # 원본 암호문
    password = list(map(int, input().split()))
    # 명령어의 개수
    C = int(input())
    # 명령어
    command = list(input().split())
    command = command

    for _ in range(C):
        # I를 발견하면 명령문이 시작한 것
        if command[0] == 'I':
            # 계속 리스트 첫 번째 숫자 가지고 작동하기 위해
            # 첫 번째 I를 없앤다
            command.pop(0)
            # x와 y는 변수에 값을 저장시키고 리스트에서 pop을 한다
            x = int(command.pop(0))
            y = int(command.pop(0))

            # y는 명령문의 길이인데, 명령문 맨 뒤부터 진행한다
            # 암호문에 명령문에 있는 암호를 하나씩 넣을때, 만약 명령문 앞에서부터 넣으면, 순서가 뒤바뀐다
            for i in range(y)[::-1]:
                # insert 통해서 암호 하나씩 넣는다
                password.insert(x, command[i])
                # 그리고 그 암호를 명령문에서 뺀다
                command.pop(i)
    
    result = ' '.join(map(str,password[0:10]))
    print(f'#{t + 1} {result}')