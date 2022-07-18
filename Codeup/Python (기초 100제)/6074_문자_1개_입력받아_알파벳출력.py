a = ord(input())
b = ord('a')

while b <= a:
    print(chr(b),end=' ')
    b += 1


# while 반복문을 쓸 것
# b는 'a'의 유니코드 => 97
# a는 입력한 값의 유니코드
# b는 a까지 도달할때까지 1씩 더해서 chr() 알파벳을 반환