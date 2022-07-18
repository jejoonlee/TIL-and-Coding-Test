# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count += 1 의 indent가 잘 안 되있음. for문 안에 포한하기 위해 tab 한번 누르기
# print(total // count)는 먼저 나눗셈의 몫을 가지고 오는것 // -> / (슬래시를 한번)
# print(total / count) 값이 소수라 float를 사용해야 한다


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(float(total / count))