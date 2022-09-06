import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    A, B = input().split()

    ans_A = sorted(A)
    ans_B = sorted(B)


    if ans_A == ans_B:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')