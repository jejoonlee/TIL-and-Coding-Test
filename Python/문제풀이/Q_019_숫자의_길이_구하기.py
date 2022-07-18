# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수 number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# number = int(input())

# if 0 < number < 10:
#     print(1)
# elif number < 100:
#     print(2)
# elif number < 1000:
#     print(3)
# else:
#     print('4자리거나 보다 많음')

a = int(input())
b = 0

while a > 0:
    a //= 10
    b += 1

print(b)