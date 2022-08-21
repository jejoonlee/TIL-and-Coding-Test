import sys
sys.stdin = open('input.txt', 'r')

# N부터 M까지의 수 중에, 0이 몇개 인지 구하는 것
# count를 사용해서 해당 숫자에 0이 몇개 있는지 구한다

T = int(input())

for t in range(T):

# N부터 M까지의 수를 뽑아낸다
    N, M = map(int, input().split())

    zero = 0
    # M미만이기 때문에, M + 1 을 한다
    for i in range(N, M + 1):
        # i 를 문자열로 만든다. .count()를 쓸 수 있게
        num = str(i)

        # num에 '0'이 있다는 조건문을 만든다
        if '0' in num:
            # zero 변수에, num에 있는 0의 갯수를 구하고
            # zero 변수에 그 갯수를 누적시킨다
            zero += num.count('0')

    print(zero)