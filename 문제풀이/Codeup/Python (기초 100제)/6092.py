n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])    # 입력된 리스트 안에 있는 str들을 int로 바꾼다
# print(a)

d = []
for i in range(24):
    d.append(0)
# print(d)        # 1~23의 갯수를 넣어줌 (다 0으로 초기됨)

for i in range (n):
    d[a[i]] += 1     # 번호를 부를때마다, 그 번호에 대한 카운트 1씩 증가
#2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가..
#  print(d)          # a에 있는 숫자들의 갯수가 리스트로 반환

for i in range(1, 24):   #카운트한 값을 공백을 두고 출력
    print(d[i], end=' ')