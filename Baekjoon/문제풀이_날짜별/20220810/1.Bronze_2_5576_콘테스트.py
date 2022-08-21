import sys
sys.stdin = open('input.txt', 'r')

# 10명 중 득점이 높은 사람에서 3명의 점수를 합산

W_uni = []
for _ in range(10):
    score = int(input())
    W_uni.append(score)

W_uni.sort(reverse = True)

K_uni = []
for _ in range(10):
    score = int(input())
    K_uni.append(score)

K_uni.sort(reverse = True)


print(sum(W_uni[0:3]), sum(K_uni[0:3]))