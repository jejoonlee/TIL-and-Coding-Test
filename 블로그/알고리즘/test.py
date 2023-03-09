import sys
sys.stdin = open('input.txt')

N, L = map(int, input().split())

pipe_location = list(map(int, input().split()))

pipe_location.sort(key=lambda x: x)

count = 0
start = 0

for i in range(1, N):

    if pipe_location[i] - pipe_location[start] > L - 1:
        count += 1
        start = i
    

print(count + 1)