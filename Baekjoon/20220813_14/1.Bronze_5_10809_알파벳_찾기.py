
letter = list(input())

alphabet = [-1] * 26

no_repeat = []
for i in range(len(letter)):
    if letter[i] not in no_repeat:
        num = ord(letter[i]) - 97
        alphabet[num] = i
        no_repeat.append(letter[i])

print(*alphabet)