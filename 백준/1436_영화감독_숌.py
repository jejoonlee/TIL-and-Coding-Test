
n = int(input())
count, answer = 0, 0

i = 666

while count < n:

    temp = str(i)

    if '666' in temp:
        count += 1

        if count == n:
            answer = i
            break
        
    i += 1

print(answer)