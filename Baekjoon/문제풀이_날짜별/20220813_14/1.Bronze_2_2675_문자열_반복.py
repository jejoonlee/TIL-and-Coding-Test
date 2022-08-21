import sys
sys.stdin = open('input.txt', 'r')

# 문자열 s를 받는다
# 문자열의 문자를 R번 반복한다

T = int(input())

for t in range(T):
    s, r = input().split()
    s = int(s)

    new_word = []
    for i in r:
        new_word.append(i * s)
    
    result = ''.join(new_word)
    print(result)