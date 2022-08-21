a = int(input())
b = int(input())

c = list(map(int, str(b)))
# int를 list로 바꾸기

print(a * int(c[2]))
print(a * int(c[1]))
print(a * int(c[0]))
print(a * b)