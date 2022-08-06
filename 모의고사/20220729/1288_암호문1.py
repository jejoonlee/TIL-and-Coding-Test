import sys
sys.stdin = open('input.txt', 'r')

# 리스트 메서드 중 .insert(삽입위치, 값)
# .insert는 리스트를 받지 못 한다. 숫자나 문자열만 가능
# if 명령어 == 'I'


# 10개의 테스트
for t in range(1, 11):

    ori_range = int(input())
    # 원본 암호문 길이

    ori = list(input().split())
    # 원본 암호문

    com_range = int(input())
    # 명령어의 개수

    com = input().split()
    # 명령어

    i = 0

    # 명령어가 끝날때까지 i를 돌린다
    while i < len(com):
        command = com[i]
        # 명령어를 순회하며 I가 있으면, 그 뒤의 숫자들을
        # 저장한다.
        # 원본 x 번째에 넣어야 하고
        # 원본에 넣아야 할 숫자들의 개수는 y개고
        # ad는 원본에 넣어야 할 숫자들이다
        if command == 'I':
            x = int(com[i + 1])
            y = int(com[i + 2])
            ad = com[i + 3 : i + y + 3]

            # 한번에 슬라이싱 한 ad 를 원본에 못 넣는다
            for a in ad[::-1]:
                ori.insert(x, a)

        i += 1

    result = ori[:10]

    print(f'#{t}', *result)