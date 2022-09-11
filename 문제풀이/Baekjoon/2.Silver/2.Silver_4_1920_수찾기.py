import sys
sys.stdin = open('input.txt')

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_dict = {}
for n in N_list:
    N_dict[n] = 0


for m in M_list:
    if m in N_dict:
        print(1)
    else:
        print(0)