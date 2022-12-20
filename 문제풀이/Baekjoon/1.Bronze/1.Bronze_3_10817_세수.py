import sys

sys.stdin = open('input.txt')

N = list(map(int, input().split()))
N.sort()

print(N[1])