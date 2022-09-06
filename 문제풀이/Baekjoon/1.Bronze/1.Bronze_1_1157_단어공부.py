# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

word = input()

cap = word.upper()

char = {}

for i in cap:
    if i in char:
        char[i] += 1
    else:
        char[i] = 1


max_value = max(char.values())

char_list = []
for key,value in char.items():
    if value == max_value:
        char_list.append(key)

if len(char_list) >= 2:
    print('?')
else:
    print(''.join(char_list))