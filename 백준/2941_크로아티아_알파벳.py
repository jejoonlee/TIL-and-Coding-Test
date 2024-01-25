
croatia = input()

words = {'c=' : 0,
         'c-' : 0,
         'dz=' : 0,
         'd-' : 0,
         'lj' : 0,
         'nj' : 0,
         's=' : 0,
         'z=' : 0
         }

wordlen = len(croatia)

i = 0
answer = 0

while i < wordlen:

    if i + 3 <= wordlen and croatia[i : i + 3] in words:
        words[croatia[i : i + 3]] += 1
        i += 2
        answer += 1
    elif i + 2 <= wordlen and croatia[i : i + 2] in words:
        words[croatia[i : i + 2]] += 1
        i += 1
        answer += 1
    else:
        answer += 1

    i += 1

print(answer)