import sys
sys.stdin = open('input.txt')

# 서류와 면접 순위를 입력받아서
# 서류 순위 위주로 먼저 오름차순으로 정렬을 한다
# 그리고 면접 순위를 비교한다
  # cnt가 1로 시작하는 이유는, 서류 1등은 등수가 제일 높은게 확정으로 합격했음
  # 면접 순위를 비교하면서, 전보다 더 작은 수를 구한다 
    # 더 작은 수를 구하면 rank라는 변수에 저장을 한다

T = int(input())

for _ in range(T):
  N = int(input())
  scores = []
  cnt = 1

  for n in range(N):
    A, B = map(int,input().split())
    scores.append((A,B))
  scores.sort()
  rank = scores[0][1]

  for j in range(1, N):
    if scores[j][1] < rank:
      rank = scores[j][1]
      cnt += 1

  print(cnt)