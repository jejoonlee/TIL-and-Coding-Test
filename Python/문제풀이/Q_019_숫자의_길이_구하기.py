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


# 123 == 100 + 20 + 3 == 100 * 1 + 10 * 2 + 3 * 1
# 123 -> 12 -> 1 -> 0
result = 0
number = 123

# 몫이 0이 되면 종료해야한다.
# 0이 되면 false이기 때문에 , '!= 0' 을 없애도 된다
while number != 0:
    number //= 10
    result += 1
print(result)



# a = int(input())
# b = 0

# while a > 0:
#     a //= 10
#     b += 1

# print(b)



# number = 123
# print(len(str(number))