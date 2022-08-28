import sys
sys.stdin = open('input.txt', encoding='utf-8')


# row와 column에서 if문에서 100을 비교하는 것이 다른 점
# row는 인덱스를 사용해서 회문을 저장했다. 즉 100이하로 설정해야, 인덱스 99번까지 슬라이싱을 한다
    # 인덱스는 0부터 시작! 이 문제에서 인덱스는 0 ~ 99
# column은 반대로 인덱스 슬라이싱이 아닌 인덱스 자체를 v_word에 저장하는 것
    # 즉 r + i는 기본적으로 0부터 99까지다!

for _ in range(10):
    q = int(input())

    # 100 x 100 글자판
    board = [list(input()) for _ in range(100)]

    words = []

    for r in range(100):
        for c in range(100):

            for d in range(100):
                # c와 d를 더할때 100 안에 들어와야 한다.
                # 리스트 밖으로 나가면 에러
                if c + d <= 100:
                    word = board[r][c : c + d]
                    # 인덱스 슬라이싱을 통해 단어들을 가지고 온다

                    # 가지고 온 단어들을 비교해서 앞 뒤가 같으면, words리스트에 넣는다
                    if len(word) >= 2:
                        if word == word[::-1]:
                            words.append(word)
            
            # column 구하기
            v_word = ''
            for i in range(100):
                #위와 같이 r + i는 100 안에 들어와야 한다
                if r + i < 100:
                    v_word += board[r + i][c]

                    if len(v_word) >= 2:
                        if v_word == v_word[::-1]:
                            words.append(v_word)

    max_length = 0
    for l in words:
        if max_length < len(l):
            max_length = len(l)

    print(f'#{q} {max_length}')