import sys
sys.stdin = open('input.txt')

N = int(input())

ropes = []

for _ in range(N):
  ropes.append(int(input()))

# 내림차순으로 정렬을 한다
# 예시) [27, 26, 25, 24]
  # 물체 중량을 제일 많이 들어올릴 수 있는 로프가 제일 먼저
  # 어차피 뒤에 로프들을 그만큼 들어올리지 못 한다
  # 27 * 1 = 27
  # 26 * 2 = 52
  # 25 * 3 = 75
  # 24 * 4 = 96
ropes.sort(reverse=True)

results = []
for n in range(1, N + 1):
  results.append(ropes[n-1] * n)

print(max(results))