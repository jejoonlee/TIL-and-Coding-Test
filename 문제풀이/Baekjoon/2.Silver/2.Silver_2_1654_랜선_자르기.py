import sys
sys.stdin = open('input.txt')

# K 이미 가지고 있는 랜선
# N 필요한 랜선
K, N = map(int, input().split())

lens = []

for _ in range(K):
    lens.append(int(input()))

start, end = 1, max(lens)

while start <= end:

    mid = (start + end) // 2
    count = 0

    for wire in lens:
        count += wire // mid

    if count >= N:
        start = mid + 1

    else:
        end = mid - 1

print(end)