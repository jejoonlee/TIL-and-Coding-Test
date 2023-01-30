import sys
sys.stdin = open("input.txt")

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(key=lambda x: -x)
answer = 0

for i in range(N):
    answer += A[i] * B[i]

print(answer)