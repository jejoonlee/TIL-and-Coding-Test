a, b = input().split()
print(a + b, sep='')

# sep='' 빈칸으로 둬서, 둘을 붙힌다

# 또는
a, b = input().split()  # 입력을 할 때, 뛰어서 써야함
reply = a + b           # reply는 a + b 이고, 공백문자 없이 덧샘을 하면 둘이 이어진다
print(reply)