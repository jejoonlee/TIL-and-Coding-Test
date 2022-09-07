import sys
sys.stdin = open('input.txt')

# 백트래킹 공부하기

# 제일 큰 수들을 찾고
# 뒤에 부터 순회하면서 제일 큰 숫자가 있으면
# 제일 앞으로 보낸다

# 32888 2 --> 88823 이 된다
# 777770 5 --> 거의 무한 반복

T = int(input())

num, cnt = input().split()

cnt = int(cnt)

num = list(num)
num_ord = sorted(num)

while cnt != 0:
    for i in range(len(num))[::-1]:
        if cnt == 0:
            break
        # 제일 큰 수를 찾아서, 앞에 그 큰 수보다 작은 수가 있으면
        # 위치를 바꾸기
        elif num[i] == num_ord[-1]:
            j = 0
            while True:
                if num[j] < num[i]:
                    num[i] = num[j]
                    num[j] = num_ord[-1]
                    num_ord.pop()
                    cnt -= 1
                    break
                else:
                    j += 1
                    if j == i:
                        num_ord.pop()
                        break
                

print(num)