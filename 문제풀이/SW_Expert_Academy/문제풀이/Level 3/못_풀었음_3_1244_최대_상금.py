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
