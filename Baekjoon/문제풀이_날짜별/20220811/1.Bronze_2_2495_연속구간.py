import sys
sys.stdin = open('input.txt', 'r')

# 연결된 숫자가 없으면 1을 출력
# 있으면 가장 긴 길이를 출력

for _ in range(3):
    num = input()

    cnt = 1

    # 연속으로 카운트한 숫자 넣기
    count = []

    # 현재 수와 다음 수를 비교하는 것
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            cnt += 1
            count.append(cnt)
        else:
            count.append(cnt)
            cnt = 1

    # 가장 긴 연속 길이를 출력
    print(max(count))