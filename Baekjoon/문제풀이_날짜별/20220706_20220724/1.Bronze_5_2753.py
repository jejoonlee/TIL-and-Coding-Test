a = int(input())

if (a % 100 == 0) != (a % 400 == 0):
    print('0')
# a가 100의 배수이지만,
# 400의 배수가 아닐때만 0을 출력
elif (a % 4 == 0):
    print('1')
else:
    print('0')