a, b = input().split()
# 공백 .split()을 이용해 입력을 한다

tmp = a
a = b
b = tmp
#입력된 값은 순서가 뒤바뀐다

print(a, b)