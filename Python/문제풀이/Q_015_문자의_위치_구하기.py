word = input()

for idx in range(len(word)):       # word를 인덱스로 순회하기
    if word[idx] == 'a':           # 순회하면서 a 를 발견하면
        print(idx)                 # idx = a 를 출력하고
        break                      # 중지한다
else:
    print(-1)                      # a가 없으면 -1 을 출력한다
                                   # for문을 다 돌았다는 뜻은
                                   # 한번도 break에 안결렸다. 즉 a는 없었다.



# 추가 문제

for idx in range(len(word)):        # range(len(word))으로 인덱스 기준으로 순회
    if word[idx] == 'a':            # 값이 'a'를 만날때마다   
        print(idx, end=' ')                  # print(idx, word[idx])는 (index, 값) 이 출력된다

# 풀이 2
result = []
for idx in range(len(word)):        
    if word[idx] == 'a':
        result.append(idx)               
        print(result)                     