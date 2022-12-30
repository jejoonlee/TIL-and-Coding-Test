import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())

    phone = []

    for n in range(N):
        phone.append(input())
        flag = True

    phone.sort()

    print(phone)

    for p in range(len(phone) - 1):
        if phone[p] == phone[p + 1][0:len(phone[p])]:
            flag = False
            break

    if flag == False:
        print('NO')
    else:
        print('YES')