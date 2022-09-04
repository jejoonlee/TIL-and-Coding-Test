a = int(input())

if a < 0 and a % 2 == 0:
    print('A')
elif a < 0 and a % 2 != 0:
    print('B')
elif a < 0 and a % 2 == 0:
    print('C')
else:
    print('D')

a = int(input())
if a < 0:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')