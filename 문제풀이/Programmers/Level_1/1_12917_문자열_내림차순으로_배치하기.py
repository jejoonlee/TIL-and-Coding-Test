
s = "Zbcdefg"

num = []
for S in s:
    num.append(ord(S))

num.sort(reverse=True)

answer = []
for i in num:
    answer.append(chr(i))

print(''.join(answer))