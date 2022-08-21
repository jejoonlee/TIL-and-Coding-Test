import sys
sys.stdin = open('input.txt', 'r')

# 각 반의 학생의 수학 성적의
# 최대 점수, 최소 점수, 점수 차이를 구한다

T = int(input())

for t in range(1, T + 1):

    grades = list(map(int, input().split()))

    # 최대 점수 구하기
    max_num = 0
    for i in range(1, len(grades)):
        if grades[i] > max_num:
            max_num = grades[i]

    # 최소 점수 구하기
    min_num = grades[1]
    for i in range(1, len(grades)):
        if grades[i] < min_num:
            min_num = grades[i]

    # 점수 차이 구하기
    grade = grades.pop(0)
    grades.sort(reverse = True)

    largest_gap = 0
    for g in range(len(grades) - 1):
        if grades[g] - grades[g + 1] > largest_gap:
            largest_gap = grades[g] - grades[g + 1]

    print(f'Class {t}')
    print(f'Max {max_num}, Min {min_num}, Largest gap {largest_gap}')