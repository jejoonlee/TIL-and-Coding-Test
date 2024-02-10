import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split(' ')))
gas = list(map(int, input().split(' ')))

cost, answer = gas[0], 0

for i in range(n - 1):
    if gas[i] < cost:
        cost = gas[i]
    
    answer += cost * dist[i]

print(answer)