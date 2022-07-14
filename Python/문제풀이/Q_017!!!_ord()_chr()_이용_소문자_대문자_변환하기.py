word = input()

for s_al in range(len(word)):            # 받은 input을 index로 순환
    if ord(word[s_al]):                  # 순환 할 때마다, 소문자 알파벳을 유니코드로 변환
        l_al = chr(ord(word[s_al])-32)   # 유니코드로 변환된 코드들을 32씩 뺀 후, 다시 대문자 알파벳으로 변환
        print(l_al, end ='')              # end = '' 한 줄로 출력