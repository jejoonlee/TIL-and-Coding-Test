import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for t in range(1, T + 1):
# 학생수 N , 학점을 알고싶어하는 학생의 번호
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())

    scores = [list(map(int, input().split())) for _ in range(N)]

    # 최종 '점수'들을 final_scores 리스트에 저장하기
    final_scores = []
    for i in range(N):
        final_score = (scores[i][0] * 0.35) + (scores[i][1] * 0.45) + (scores[i][2] * 0.2)
        final_scores.append(round(final_score, 3))

    # 최종 '점수'들을 내림차순으로 rank로 저장하기
    rank = sorted(final_scores, reverse = True)

    for i in range(len(rank)):
        if final_scores[K - 1] == rank[i]:
            g = int(i // (N / 10))
            grade = grades[g]
    
    print(f'#{t} {grade}')