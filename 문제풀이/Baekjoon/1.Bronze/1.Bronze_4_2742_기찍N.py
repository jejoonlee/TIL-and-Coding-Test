# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())

for i in range(n, 0, -1):
# i는 n이하 0초과로 '-1' 뒤로 하나씩 추출
    print(i)