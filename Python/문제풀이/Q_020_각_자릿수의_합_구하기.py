a = input()
list = list(map(int, str(a)))
# # str(a) 입력된 a를 문자열로 만든다
# # map() 문자열인 a를 int로 반환한다
# # 리스트 객체를 만든다

add = sum(list)

print(add)

# a = input()
# al = str(a)
# all = list(map(int, str(a)))

# print(all, type(all))