y, m, d = input().split('.')
# y m d 사이에 '.' 가 있어야 입력이 된다

tmp = y
y = d
d = tmp
# y가 d의 자리로 가고 d는 y 자리로 가게 된다

print(int(y), int(m), int(d), sep=('-'))
# 출력은 d, m , y 순서대로 출력되고, 사이에 '-'가 들어간다