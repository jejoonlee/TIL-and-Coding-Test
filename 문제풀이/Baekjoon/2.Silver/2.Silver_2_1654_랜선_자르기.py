import sys
sys.stdin = open('input.txt')

# K 이미 가지고 있는 랜선
# N 필요한 랜선
K, N = map(int, input().split())

lens = []

for _ in range(K):
    lens.append(int(input()))

M = min(lens) + 1
count = 0

# N개 이상일 때 while문을 끝낸다
# count는 만들 수 있는 랜선 개수

# while문은 
# 가지고 있는 랜선 중 길이가 제일 짧은 랜선으로 시작해서, 1씩 내려가면서
# 총 몇개의 랜선을 만들 수 있는지

while count < N:
    M -= 1
    count = 0

    for i in lens:
        count += i // M
    

print(M)