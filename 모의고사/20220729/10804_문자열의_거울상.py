
T = int(input())

for t in range(1, T + 1):
    # 문자열 입력
    s = input()
    # 문자열을 인덱스를 이용하여 반대로 돌리기
    rev_s = s[::-1]

    letters = []
    # b면 d로 / d면 b로 / p면 q로 / q면 p로 변환해야한다
    # 단어 하나씩 순회하면서, 바꾸고, 리스트에 넣어준다
    for letter in rev_s:
        if letter == 'q':
            letter = letter.replace('q', 'p')
            letters.append(letter)
        elif letter == 'p':
            letter = letter.replace('p', 'q')
            letters.append(letter)
        elif letter == 'd':
            letter = letter.replace('d', 'b')
            letters.append(letter)
        elif letter == 'b':
            letter = letter.replace('b', 'd')
            letters.append(letter)
    
    # .join을 통해서 str으로 반환
    result = ''.join(letters)

    print(f'#{t} {result}')