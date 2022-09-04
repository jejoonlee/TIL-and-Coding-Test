import sys
sys.stdin = open('input.txt')

# 평점을 같은 비율로 부여
# K번째 학생의 학점 출력
T = int(input())

grade = {0 : 'A+', 1 : 'A0', 2 : 'A-', 3 : 'B+', 4 : 'B0', 5 : 'B-', 6 : 'C+', 7 : 'C0', 8 : 'C-', 9 : 'D0'}

for t in range(1, T + 1):
    N, K = map(int, input().split())

    students = []
    for n in range(N):
        m, f, task = map(int, input().split())
        score = (m * 0.35) + (f * 0.45) + (task * 0.2)
        students.append(score)

    rank = sorted(students, reverse = True)

    # num은 주어진 N개 중 10개로 몇 묶음이 묶이는지 계산
    num = N // 10
    # g는 K의 총점의 순서가 몇 번째인지 계산한다
    g = rank.index(students[K - 1])
    # g를 num으로 나누면 grade의 번호가 나온다
    grade_id = g // num

    # grade 번호가 나온 것을 딕셔너리를 탐색하면 된다
    print(f'#{t} {grade[grade_id]}')