import sys
sys.stdin = open('input.txt', 'r')

vowel = 'aeiouAEIOU'

while True:
    cnt = 0

    sen = input()

    if sen == '#':
        break

    for i in sen:
        if i in vowel:
            cnt += 1


    print(cnt)