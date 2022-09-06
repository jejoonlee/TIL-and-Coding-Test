# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())

for i in range(1, n + 1):
    # range 1부터 n을 하면 n 미만이다. 
    # n + 1을 해서 n 이하로 만든다
    print(i)