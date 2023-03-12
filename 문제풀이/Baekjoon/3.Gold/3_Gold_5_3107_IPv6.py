import sys
sys.stdin = open('input.txt')

IPv6 = list(input().split(':'))
answer = []
add_address = 0

if IPv6[0] == '':
    IPv6.pop(0)
if IPv6[-1] == '':
    IPv6.pop()

if len(IPv6) == 8:
    for i in IPv6:
        answer.append(i.zfill(4))

elif len(IPv6) > 0:
    for index in range(len(IPv6)):

        if len(IPv6[index]) != 0:
            answer.append(IPv6[index].zfill(4))

        else:
            while len(IPv6) + add_address <= 8:
                answer.append("0000")
                add_address += 1

print(':'.join(answer))