import sys
sys.stdin = open('input.txt')

# 제일 큰 수들을 찾고
# 뒤에 부터 순회하면서 제일 큰 숫자가 있으면
# 제일 앞으로 보낸다

T = int(input())

num, cnt = input().split()

cnt = int(cnt)

num = list(num)
num_ord = sorted(num)

while cnt != 0:
    for i in range(len(num))[::-1]:

        # 제일 큰 수 구하기
        if num[i] == num_ord[-1]:
            j = 0
            if num[j] < num[i]:
                num[i] = num[j]
                

print(num)