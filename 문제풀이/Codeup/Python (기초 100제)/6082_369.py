a = int(input())


for i in range(1, a + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end = ' ')
    else:
        print(i, end = ' ')

# if문에서 10을 나눠서 3, 6, 9 가 남으면 X 표시를 하고
# 그 외에는 숫자를 적어준다