import sys

input = sys.stdin.readline

n = int(input())
dance = {}

for _ in range(n):
    nOne, nTwo = map(str, input().split(' '))
    nOne, nTwo = nOne.strip(), nTwo.strip()

    if nOne == 'ChongChong' or nTwo == 'ChongChong':
        if nOne not in dance or nTwo not in dance:
            dance[nOne], dance[nTwo] = 1, 1

    elif 'ChongChong' in dance and (nOne in dance or nTwo in dance):
        if nOne not in dance: dance[nOne] = 1
        elif nTwo not in dance: dance[nTwo] = 1

print(len(dance))