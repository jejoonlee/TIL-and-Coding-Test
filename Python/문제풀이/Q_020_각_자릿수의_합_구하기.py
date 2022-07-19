# a = input()
# list = list(map(int, str(a)))
# # # str(a) 입력된 a를 문자열로 만든다
# # # map() 문자열인 a를 int로 반환한다
# # # 리스트 객체를 만든다

# add = sum(list)

# print(add)



a = int(input())
result = 0

while a:
    result += a % 10
    a //= 10
print(result)

# 3.
# divmod(x,y)는 x를 y로 나누고,
# 결과를 tuple로 반환
# 몫, 나머지
number, reminder = divmod(number, 10)
result += reminder
print(result)