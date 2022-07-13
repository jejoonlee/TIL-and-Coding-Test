# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.

word = 'happy!'

count = 0               # h a p p y ! 하나하나의 변수
for i in word:
    count += 1          # 1씩 증가
print(count)

# ‘happy!’ 는 하나의 통
# count는 0으로 시작하면서, 주어진 list가 하나씩 출력될 때마다 count는 하나 씩 증가
# happy! 가 다 사라질 때까지 count는 순환한다