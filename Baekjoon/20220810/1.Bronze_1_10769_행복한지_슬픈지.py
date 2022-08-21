
sentence = input()

smile = sentence.count(':-)')
sad = sentence.count(':-(')

if smile > sad:
    print('happy')
elif smile == 0 and sad == 0:
    print('none')
elif smile == sad:
    print('unsure')
elif sad > smile:
    print('sad')