# int를 str으로 변환해서 풀기... 했는데 ㅜ.ㅜ
T = int(input())

for i in range(1, T + 1):
    n = int(input())      # n의 숫자 입력
    n1 = n
    result = set()
    while True:     # set의 길이가 10개 미만일때
        for idx in str(n):      # n을 str로 만든다
            result.add(idx)
        if len(result) == 10:
            break
        n = n + n1              # 'n1'은 'n'의 고정 값이다 
    print(f'#{i}', n)