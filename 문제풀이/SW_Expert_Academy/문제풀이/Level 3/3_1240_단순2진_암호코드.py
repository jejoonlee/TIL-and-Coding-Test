import sys
sys.stdin = open('input.txt')

def pprint(st):
    for i in st:
        print(i)
    print('-------------------------')

T = int(input())

M, N = map(int, input().split())

password = [list(input()) for _ in range(M)]

pprint(password)