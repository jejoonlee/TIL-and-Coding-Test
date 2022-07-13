# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
# apple

word = 'apple'
rm_a = ''

for i in word:
    if i == 'a':
        continue        # continue를 이용해서 a와 일치하면, 지나간다
    rm_a += i
    
print(rm_a)

word = 'apple'
rm_a = ''

for i in word:
    if i != 'a':        # continue를 이용해서 a와 일치하면, 지나간다
        rm_a += i
    
print(rm_a)