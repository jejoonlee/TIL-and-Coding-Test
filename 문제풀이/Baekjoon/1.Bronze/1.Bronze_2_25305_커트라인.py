import sys
sys.stdin = open('input.txt')

# N명의 학생들이 응시를 했고
# k 명이 상을 받는데
# k 명 중 점수가 제일 낮은 사람을 찾는 것

N, K = map(int, input().split())

scores = list(map(int, input().split()))

# 내림차순으로 정렬한다
scores.sort(reverse = True)

# 인덱스는 0부터 시작하기 때문에, K에서 1을 뺀
# 인덱스의 수가 답이다
print(scores[K - 1])