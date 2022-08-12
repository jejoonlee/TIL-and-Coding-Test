import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

vowel = 'aeiou'

for t in range(1, T + 1):
    word = input()

    # 모음이 없는 letter들만 new_word에 넣기
    new_word = []
    for i in word:
        if i not in vowel:
            new_word.append(i)
    
    result = ''.join(new_word)
    print(f'#{t} {result}')