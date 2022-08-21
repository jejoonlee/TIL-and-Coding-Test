import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for i in range(T):
    N = int(input())
    N_num = set(list(map(int, input().split())))
    M = int(input())
    M_num = list(map(int, input().split()))

    for i in M_num:
        if i in N_num:
            print(1)
        else:
            print(0)