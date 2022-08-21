# 주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다. 
# 얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.

taebo = list(input())

left = []

for i in taebo:
# 왼쪽부터 순회
    if i == '(':
        break
        # 왼쪽부터 순회하다 '('를 보면 멈춤
    elif i == '@':
    # 순회하다 @를 발견하면 리스트에 넣는다
        left.append(i)

right = []

for i in taebo[::-1]:
# 오른쪽부터 순회하고 내용은 위랑 같다
    if i == ')':
        break
    elif i == '@':
        right.append(i)

print(len(left), len(right))