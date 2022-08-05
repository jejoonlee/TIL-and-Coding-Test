import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

# 테스트 케이스 수
for t in range(1, T + 1):
    # 수강생 수, 과제 제출
    stu, hom = map(int, input().split())
    # 과제 제출한 학생
    fin = list(map(int, input().split()))

    # 과제를 제출하지 않은 사람 번호 넣기
    unfin = []
    # 수강생 번호
    for i in range(1, stu + 1):
        if i not in fin:
            unfin.append(i)
            result = sorted(unfin)
            result = ' '.join(map(str, result))

    print(f'#{t} {result}')