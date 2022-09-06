import sys
sys.stdin = open('input.txt')

T = int(input())
cnt = 0

for t in range(T):

    word = list(input())

    flag = True
    straight = []
    for w in word:
        # w가 straight에 없을 경우와 straight의 마지막이랑 똑같을 경우
        if w not in straight or straight[-1] == w:
            straight.append(w)
        else:
            flag = False
            break

    if flag == True:
        cnt += 1

print(cnt)