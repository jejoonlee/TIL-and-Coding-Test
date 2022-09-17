import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    wood = int(input())

    if wood % 2 == 0:
        print(f'#{t} Alice')
    else:
        print(f'#{t} Bob')