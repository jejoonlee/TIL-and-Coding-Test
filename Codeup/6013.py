from os import TMP_MAX


a = input()
b = input ()

tmp = a
a = b
b = tmp
# tmp 라는 임시 변수를 만든다
# a의 값은 -> tmp로
# b의 값은 -> a 로 (a 값은 tmp로 갔기 때문에, 현재 비어있음)
# 마지막으로 tmp에 있던 원래 a값은 b로 가게 된다

print(a)
print(b)