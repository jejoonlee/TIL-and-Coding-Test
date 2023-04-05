import sys
sys.stdin = open('input.txt')


flag = True
al_dict = {}
alp = input()

for a in alp:
    if a in al_dict:
        al_dict[a] += 1 
    else:
        al_dict[a] = 1

if sum([al % 2 for al in al_dict.values()]) > 1:
    flag = False
else:
    answer, result, half = '', '', ''

    for key, value in sorted(al_dict.items()):
        result += key * (value // 2)

        if value % 2 == 1:
            half += key

    answer = result + half + result[-1::-1]
    

if flag == False:
    print("I'm Sorry Hansoo")
else:
    print(answer)