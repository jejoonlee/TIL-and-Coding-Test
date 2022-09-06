import sys
sys.stdin = open('input.txt')

# 제일 중요한 것은 56개의 숫자를 찾는 것
# 모든 암호에는 뒷부분이 1이 있다. 그래서 2차원 리스트를 뒤로 순회하면서 1을 찾는 것이 제일 중요


T = int(input())

# 이걸 딕셔너리로 만들어도 된다
pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for t in range(1, T + 1):
    M, N = map(int, input().split())

    password = [list(input()) for _ in range(M)]

    code = []

    # 56개의 암호화 숫자들을 찾게 되면, 더 이상 순회를 안 해도 된다
    # 즉 56번을 센다면, 이차원 순회는 끝
    cnt = 0

    for i in range(M)[::-1]:
        for j in range(N)[::-1]:
            if cnt == 56:
                break

            # 1을 발견하면, 그 발견한 지점에서 55를 뺀다 (반대로 순회를 했기 때문에)
            # 그리고 55를 뺀 지점부터 for문을 통해 code 리스트에 저장을 한다
            if password[i][j] == '1':
                for k in range(56):
                    num = j - 55
                    code.append(password[i][num + k])
                    cnt += 1

    # 그리고 code리스트에 있는 암호들을 7개씩 뺀고, pattern과 배교하여, pattern의 인덱스를
    # result에 저장을 한다
    # 여기서 pattern의 인덱스가 암호를 풀면 나오는 정수다
    result = []
    while len(code) != 0:
        code_nums = ''
        for _ in range(7):
            a = code.pop(0)
            code_nums += a

        if code_nums in pattern:
            result.append(pattern.index(code_nums))

    # 인덱스이기 때문에 문제 기준에서 짝수는 홀수가 되고, 홀수는 짝수가 된다
    final = 0
    for ind in range(8):
        if ind % 2 == 0:
            final += result[ind] * 3
        else:
            final += result[ind]

    if final % 10 == 0:
        print(f'#{t} {sum(result)}')
    else:
        print(f'#{t} 0')