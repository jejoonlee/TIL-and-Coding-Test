import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):

    green = input()
    cnt = 0

    for i in range(len(green)):
        if green[i] == '(':
            if green[i + 1] == ')' or green[i + 1] == '|':
                cnt += 1

        elif green [i] == ')':
            if green[i - 1] == '|':
                cnt += 1

    print(f'#{t} {cnt}')
