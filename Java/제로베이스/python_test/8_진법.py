
# bin : 2진수
# oct : 8진수
# hex : 16진수
# 반환 타입은 문자열

dNum = 30

print(f'2진수 : {bin(dNum)[2:]}')
print(f'8진수 : {oct(dNum)[2:]}')
print(f'16진수 : {hex(dNum)[2:]}')

print(f'2진수 : {bin(dNum)}')
print(f'8진수 : {oct(dNum)}')
print(f'16진수 : {hex(dNum)}')


# x진수에서 10진수로 바꿀 때 (int를 사용해주면 된)
print(f'2진수에서 10진수로 : {int(bin(dNum), 2)}')
print(f'8진수에서 10진수로 : {int(oct(dNum), 8)}')
print(f'16진수에서 10진수로 : {int(hex(dNum), 16)}')
