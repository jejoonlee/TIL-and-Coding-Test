# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
# input: apple
# output: elppa

word = 'apple'
back = word[::-1]   # 맨 뒤에서부터 -1씩 출력

print(back)


word = 'apple'
result = ''

for char in word:
    result = char + result  # 원래 result = result + char 에서 result = char + result
print(result)               # 로 바꿔서 진행하면, 단어가 반대로 출력된다

# 3. index
# 익숙해질수록 나중에 알고리즘 코드 풀기 좋다
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')      

# sep ('')= 여러개를 동시에 출력할 때 사이에 구분값
# end ('\n') = print 출력이 된 이후 뒤에 뭐를 붙일지!